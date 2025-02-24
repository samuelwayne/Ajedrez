# CheckMate

Backend del juego de ajedrez creado por  [@samuelwayne](https://github.com/samuelwayne) e [@ismola](https://github.com/Ismola)


> [!NOTE]
> Proyecto padre: https://github.com/Ismola/chess_game_app
>
> Web: https://chessgame.ismola.dev/


## Tecnologías
* Python
  * Flask

## Roadmap

### Fase 1 Movimiento de fichas

> [!NOTE]
> En esta fase se puede conseguir un ajedrez, multijugador local

#### Samu - Backend

- Endpoint para obtener posibles movimientos de una ficha
  - Definir estructura del objeto tablero
  - Definir estructura del envío de informacion entre cliente y servidor
    > Saber como quieres que te envíen los datos desde el cliente y como se los vas a devolver. Tiene que ser un [json](https://www.json.org/json-es.html) en ambos casos
  - Definir funciones de movimiento por cada pieza
    - Primero otorgar el movimiento básico de la pieza dentro de los límites del tablero, sin tener en cuenta otras piezas ni movimientos excepcionales (primer movimientos de peones, enroques, comer, etc)
    - Tener en cuenta otras piezas
      - Cuando son del mismo color
      - Cuando son de distinto color (comer)
    - Movimientos excepcionales

#### Isma - Frontend

- Elegir tecnología
- ✅ DevContainers
- [Pintar](https://chessboardjs.com/)

> [!WARNING]
> ¿Le meto 3D o 2D?

### Fase 2 Despliegue

> [!NOTE]
> En esta fase se despliega a internet

#### Isma - Deploy

- Dockerizar backend
- Front en netlify con subdominio.ismola.dev

> [!WARNING]
> Elegir o dominio o subdominio

- Backend, en algun servidor(v1) o algún sitio que desplieguen imagenes de docker gratis

### Fase 3 Multijugador online

#### Isma - Backend

> [!NOTE]
> En esta fase se crea el modo online. La comunicacion entre jugadores será a traves de websocket pasando por servidor, que guarda el movimiento en la base de datos. Además, desde cualquier dispositivo se podrá seguir la partida a traves de un link.

- Meter websockets

#### Samu - Backend

- Guardar id de partida en DB, junto con el websocket.id de blancas y websocket.id de negras
- Guardar en DB tablero, e historial de partidas
  - Definir modelo de DB

#### Isma - Front

- Comunicacion con websocket
- Cookies


## How to start the project

### Create a Virtual Environment

We use a module named virtualenv which is a tool to create **isolated Python environments**. Virtualenv creates a folder that contains all the necessary executables to use the packages that a Python project would need.

```bash
python3 -m venv <whatever_virtual_environment_name>
```

### Activate virtual environment

```bash
source <whatever_virtual_environment_name>/bin/activate   # for Unix/Linux
.\<whatever_virtual_environment_name>\Scripts\activate    # for Windows
```

### Install project libraries

```bash
pip install -r requirements.txt  # Works for both Unix/Linux and Windows
```

### Run main file

```bash
python3 main.py  # for Unix/Linux
python main.py   # for Windows
```

Now, the server is accessible at `http://localhost3000`

### First Call

![First Call](https://github.com/Ismola/selenium-scraper-quickstarter/blob/main/readmeImages/firstcall.png?raw=true)

![Auth Call](https://github.com/Ismola/selenium-scraper-quickstarter/blob/main/readmeImages/authcall.png?raw=true)

### Make your firsts changes

1. The first thing is to add your .env file. You can add a invented bearer token to get started

2. Then configure the base url in the utils/config.py file

3. In order to work on your project, you must add an endpoint to main.py.

4. Next, create a controller, and add the different web actions on the controller. It is recommended to do actions with few steps, to be able to modularize your code, and not repeat code in the future.