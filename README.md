# Piloto de Registro de Permisos

Este sistema permite registrar permisos de acceso en nubes (GCP, Azure, OCI), almacenarlos en CSV y exportarlos a Excel.

## 🚀 Despliegue Automático

Para crear una nueva VM en Azure con todo configurado:

1. Crea una nueva **VM Ubuntu** (Ubuntu 22.04 recomendado).
2. En la sección **Advanced → Custom data**, pega el contenido del archivo **cloud-init/cloud-init.yaml**.
3. Completa la creación de la VM.
4. Espera unos minutos hasta que la VM esté configurada automáticamente.

### Rutas disponibles:

- **/guardar**: Registrar un nuevo permiso (POST).
- **/listar**: Ver los registros de permisos (GET) en formato JSON.
- **/descargar**: Descargar todos los registros como archivo Excel (GET).

### Logs y Datos

Los registros se guardan en **/opt/piloto/data/permisos.csv** y los logs de la aplicación en **/opt/piloto/data/app.log**.

---

## 📁 Estructura del repositorio



permiso-piloto/
│
├── frontend/
│ └── index.html # Formulario de registro
├── backend/
│ ├── app.py # Código de la aplicación Flask
│ └── requirements.txt # Dependencias de Python
├── cloud-init/
│ └── cloud-init.yaml # Script de configuración de la VM
└── README.md # Documentación


---

## 🛠 Cómo funciona

### 1. **Formulario de Registro**  
El formulario en **index.html** permite ingresar permisos. Los datos se envían a la ruta **/guardar**.

### 2. **Ver los registros**  
Accede a la ruta **/listar** para obtener los registros en formato JSON.

### 3. **Descargar Excel**  
Accede a **/descargar** para obtener un archivo `.xlsx` con todos los registros de permisos.


