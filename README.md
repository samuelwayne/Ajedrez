# CheckMate

Un juego de ajedrez creado con Python. Por samuel_wayne y ismola.

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
- DevContainer
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
