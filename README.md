📄 CONTENIDO COMPLETO DE README.md
# 🚀 Piloto de Registro de Permisos en la Nube  

Sistema simple para registrar permisos creados en GCP / Azure / OCI sin depender de ServiceNow.  
Incluye:

- Frontend HTML  
- Backend Python/Flask  
- Almacenamiento en CSV local  
- Cloud-init para desplegar automáticamente en Azure  
- Infraestructura 100% reproducible usando Git  

---

# 📁 Estructura del repositorio



permiso-piloto/
│
├── frontend/
│ └── index.html
│
├── backend/
│ ├── app.py
│ └── requirements.txt
│
├── cloud-init/
│ └── cloud-init.yaml
│
└── README.md


---

# 🟢 ¿Qué hace este sistema?

Permite registrar:

- Número de ticket  
- Fecha  
- Usuario o Grupo  
- Acción realizada (crear grupo, asignar rol, modificar rol, etc.)  
- Rol asignado o creado  
- Permisos aplicados  
- Proyecto / Contexto  
- Responsable técnico  

Cada registro se guarda automáticamente en:



/opt/piloto/data/permisos.csv


Esto crea un **rastro de auditoría simple y consultable**.

---

# 🛠 Cómo desplegar la VM en Azure (Automático)

### 1️⃣ Crear una VM Ubuntu en Azure  
- Distribución recomendada: **Ubuntu 22.04**  
- Tamaño: B1s es suficiente  
- Autenticación: SSH o password  

### 2️⃣ En la creación, ir a:  
**Advanced → Custom data**

### 3️⃣ Pegar el contenido del archivo:  
`cloud-init/cloud-init.yaml`

Ese archivo:

- Instala nginx  
- Instala Python3  
- Crea carpetas  
- Descarga el frontend y backend desde GitHub  
- Instala Flask  
- Configura nginx como reverse proxy  
- Crea un servicio systemd para Flask  
- Arranca todo automáticamente  

### 4️⃣ Crear la VM

### 5️⃣ Abrir en el navegador:  


http://<IP_PUBLICA>


---

# 👨‍💻 Funcionamiento

### 🔹 Frontend  
El formulario HTML envía los datos a:



POST /guardar


### 🔹 Backend (Flask)  
El backend:

- recibe los datos del formulario  
- escribe una línea en el CSV  
- responde con “Permiso registrado correctamente”  

### 🔹 CSV  
El archivo queda en:



/opt/piloto/data/permisos.csv


Para verlo:



sudo cat /opt/piloto/data/permisos.csv


---

# 🔄 Cómo actualizar la VM con nuevos cambios del repo

Si modificas `index.html` o `app.py`:

1. Haces commit + push  
2. En la VM reinicias:



sudo systemctl restart piloto_flask
sudo systemctl restart nginx


O simplemente vuelves a crear una VM con el mismo cloud-init.  
Azure instalará la última versión del repo automáticamente.

---

# 🔍 Logs útiles

### Ver estado del backend:


sudo systemctl status piloto_flask


### Logs en vivo:


sudo journalctl -u piloto_flask -f


### Logs de nginx:


sudo tail -f /var/log/nginx/error.log


---

# 🧪 Probar backend manualmente



curl -X POST http://localhost:5000/guardar
 -d "ticket=123"


---

# ☁ Ideas futuras (opcionales)

- Página `/listar` para ver todos los registros en tabla  
- Exportación a Excel  
- Envío automático a Azure Storage  
- Autenticación simple para evitar uso público  
- Reemplazar CSV por SQLite  

---

# ✔ ¿Quieres que te agregue la página `/listar` + backend para mostrar los permisos?
Dímelo y te la dejo lista.
