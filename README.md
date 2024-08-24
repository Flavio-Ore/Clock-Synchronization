# Clock synchronization using Christian's algorithm method 

Distributed Systems course assignment to synchronize the server clock with the client using Christian's algorithm.

The Demo run the server in a Linux Mint laptop using python3 and the client in a Windows 10 desktop using nodejs.
[Video demo](https://www.canva.com/design/DAGOzs7n6dw/saIhZ3vpTWiQYSG-lECSRA/edit?utm_content=DAGOzs7n6dw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) made in Canva.

## Setup
```bash
git clone https://github.com/Flavio-Ore/Clock-Synchronization.git
cd .Clock-Synchronization
```

## Server side
> [!TIP]
> It is recommended to run the server on a different machine but on the same LAN.

### For the Python server
It is necessary to have the `3.11.X` version of Python installed.

We proceed to enter the folder and run the server clock.
```bash
cd .server
python3 main.py
```

## Client side
Depending on the client you want to use.
The python client will display the results in the console.
The nodejs client creates an http server and will serve an `index.html` page that consumes the API that communicates with the clock python server.

### For the Nodejs client
You need to have `v20.X.X.X` version of Nodejs and `10.X.X` version of npm installed.

```bash
cd .\client Nodejs
```

Install the dependencies with `npm i`.

To run the client server
```bash
node --watch .\server.cjs
```

### For the Python3 client
You need to have Python version ``3.11.X`` and pip version ``24.X.X.X`` installed.
This module requires to raise a ``virtual environment``.

```bash
cd .\client\python\
py -m venv venv
# Activate the venv
.\venv\Scripts\activate
(venv) pip install python-dateutil
(venv) python main.py
```

## Other sources of information
- [Cristian's algorithm - geeksforgeeks](https://www.geeksforgeeks.org/cristians-algorithm/)
