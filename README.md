# Proyecto ST0263: Red P2P

Este proyecto implementa una red P2P descentralizada que soporta las siguientes funcionalidades:
- **Conexión y desconexión de nodos (`join` y `leave`).**
- **Búsqueda de archivos en la red.**
- **Almacenamiento y recuperación de archivos (`put` y `get`).**

## Estructura del proyecto
client/: Código del cliente.
server/: Código del servidor con los microservicios.
protos/: Archivos .proto para gRPC.
docker/: Archivos Docker para despliegue.
tests/: Pruebas automatizadas.