# Registro de Permisos Cloud - Piloto

Sistema simple para registrar accesos/permisos aplicados en GCP, Azure y OCI, con backend Flask, frontend HTML y almacenamiento local en CSV.

## 🚀 Despliegue Automático

Este repositorio incluye un archivo `cloud-init.yaml` que permite:

- Instalar Nginx, Python y dependencias
- Crear estructura del proyecto
- Descargar el frontend y backend desde GitHub
- Iniciar Flask como servicio systemd
- Configurar Nginx como reverse proxy

### Cómo usar

1. Crear una VM Ubuntu en Azure.
2. Ir a la sección **Advanced → Custom data**.
3. Pegar el contenido del archivo:

