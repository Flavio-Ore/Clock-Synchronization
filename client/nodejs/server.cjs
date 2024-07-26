const { Socket } = require('net')
const morgan = require('morgan')
const { DateTime } = require('luxon')
const express = require('express')

function httpServer () {
  const PORT = process.env.PORT ?? 5555
  const app = express()
  app.use(morgan('dev'))

  app.get('/', (req, res) => {
    res.sendFile(`${__dirname}/index.html`)
  })

  app.get('/time', (req, res) => {
    res.status(200).send({ isoTime: DateTime.now().toISO() })
  })

  app.get(`/cristian-algorithm`, (req, res) => {

    const socket = new Socket()
    const SERVER_PORT = 3333
    const SERVER_ADDRESS = '192.168.1.44'

    socket.connect({ port: SERVER_PORT, host: SERVER_ADDRESS }, () => {
      const T0 = process.hrtime.bigint()

      socket.on('data', data => {
        const Tserver = DateTime.fromISO(data.toString())
        const T1 = process.hrtime.bigint()

        const clientTime = DateTime.now().toISO()
        console.log({ Tserver: Tserver.toString() })
        console.log({ Tclient: clientTime.toString() })

        console.log({ T0 })
        console.log({ T1 })

        const RTT = T1 - T0
        console.log(`Round Time Trip Latency: ${RTT} nanoseconds`)

        //! Calcula el tiempo de sincronización
        const Tclient = Tserver.plus({
          milliseconds: RTT / 2n / 1_000_000n
        })

        console.log(`Client synchronized time: ${Tclient.toString()}`)

        //! Calcula el error de sincronización
        const Terror = RTT / 2n
        console.log(
          `Synchronization error: ${Terror / 1_000_000n} milliseconds`
        )

        res
          .status(200)
          .send({ clientTime, Tserver, Tclient, Terror: Terror.toString() })
        socket.destroy()
      })

      socket.on('error', error => {
        console.error(error)
        res.status(500).send({ error: 'Internal Server Error' })
      })
    })
  })

  app.use((req, res) => {
    res.status(404).send('<h1>404 Not Found</h1>')
  })

  app.listen(PORT, () => {
    console.log('Listening on port http://localhost:' + PORT)
  })
}

httpServer()
