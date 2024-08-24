# Sincronización del reloj usando el algoritmo de Christian

Tarea del curso de Sistemas Distribuidos para sincronizar el reloj del servidor con el cliente usando el algoritmo de Christian.
La Demo ejecuta el servidor en una laptop Linux Mint usando python3 y el cliente en Windows 10 usando nodejs.
[Video demostración](https://www.canva.com/design/DAGOzs7n6dw/saIhZ3vpTWiQYSG-lECSRA/edit?utm_content=DAGOzs7n6dw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) hecho en Canva.

## Setup
```bash
git clone https://github.com/Flavio-Ore/Clock-Synchronization.git
cd .\Clock-Synchronization\
```

## Servidor
Se recomienda ejecutar el servidor en una máquina diferente pero que estén en la misma LAN.

### Para el servidor Python
Necesitas tener instalado Python versión `3.11.X`

Procedemos a entrar a la carpeta y ejecutar el servidor reloj.
```bash
cd .\server
python3 main.py
```

## Cliente
Dependiendo del cliente que desees usar.
EL cliente python mostrará los resultados en la consola.
El cliente nodejs crea un servidor http y servirá una página `index.html` que consume la API que se comunica con el servidor reloj en python.

### Para el cliente Nodejs
Necesitas tener intalado Nodejs versión `v20.X.X` y npm versión `10.X.X`.

```bash
cd .\client\nodejs
```

Instalas las dependencias con `npm i`

Para ejecutar el servidor cliente
```bash
node --watch .\server.cjs
```

### Para el cliente Python3
Necesitas tener instalado Python versión `3.11.X` y pip versión `24.X.X`
Este módulo requiere levantar un "virtual environment".

```bash
cd .\client\python\
py -m venv venv
# Activa el venv
.\venv\Scripts\activate
(venv) pip install python-dateutil
(venv) python main.py
```

## Otras fuentes de información
- [Cristian’s Algorithm](https://www.geeksforgeeks.org/cristians-algorithm/)
