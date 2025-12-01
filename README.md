# Piloto de Registro de Permisos

Este sistema permite registrar permisos de acceso en nubes (GCP, Azure, OCI), almacenarlos en un archivo CSV y exportarlos a Excel.

## 🚀 Despliegue Automático

Para crear una nueva VM en Azure con todo configurado:

1. Crea una nueva **VM Ubuntu** (Ubuntu 22.04 recomendado).
2. Durante la creación de la VM, en la sección **Advanced → Custom data**, pega el contenido del archivo **cloud-init/cloud-init.yaml**.
3. Completa la creación de la VM.
4. Espera unos minutos hasta que la VM se configure automáticamente con todo el sistema (incluyendo Flask, Nginx, y las dependencias).

### Rutas disponibles:

- **/guardar**: Registrar un nuevo permiso (POST).
- **/listar**: Ver los registros de permisos (GET) en formato JSON.
- **/descargar**: Descargar todos los registros como archivo Excel (GET).

### Logs y Datos

- Los registros de permisos se guardan en:  
  `/opt/piloto/data/permisos.csv`
  
- Los logs de la aplicación se almacenan en:  
  `/opt/piloto/data/app.log`

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
El formulario en **index.html** permite ingresar permisos. Los datos se envían a la ruta **/guardar** mediante un POST.

### 2. **Ver los registros**  
Accede a la ruta **/listar** para obtener los registros de permisos en formato JSON.

### 3. **Descargar Excel**  
Accede a **/descargar** para obtener un archivo `.xlsx` con todos los registros de permisos almacenados en el sistema.

---

## 🔧 Pasos para probar la app

1. **Crear VM**: Usa el archivo `cloud-init.yaml` para crear una nueva VM en Azure.  
2. **Acceder al Formulario**: Dirígete a la IP pública de la VM en tu navegador para ver el formulario de registro.
3. **Registrar Permisos**: Completa el formulario y haz clic en "Registrar". Los datos se almacenarán en un archivo CSV.
4. **Ver los Registros**: Usa la ruta **/listar** para ver todos los registros en formato JSON.
5. **Descargar los Registros**: Accede a la ruta **/descargar** para obtener un archivo Excel de todos los registros.

---

## 📚 Información adicional

- Los registros de permisos se almacenan en un archivo CSV (`/opt/piloto/data/permisos.csv`) y se pueden descargar en cualquier momento como un archivo Excel.
- Los logs de la aplicación se guardan en `/opt/piloto/data/app.log` para realizar un seguimiento de los errores o eventos importantes.
- Puedes modificar el `index.html` o el `app.py` según sea necesario y, si deseas, modificar la configuración de `cloud-init.yaml` para adaptar el despliegue.
