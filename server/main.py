import datetime as Datetime
import socket as Socket


def initiateClockServer():
    socket = Socket.socket()
    print("Socket successfully created")

    port = 3333
    host = "192.168.1.44"
    socket.bind(("", port))

    socket.listen(5)
    print("Socket is listening...")

    while True:
        connection, address = socket.accept()
        print("Server connected to", address)
        connection.send(str(Datetime.datetime.now().isoformat()).encode())
        connection.close()


if __name__ == "__main__":
    initiateClockServer()
