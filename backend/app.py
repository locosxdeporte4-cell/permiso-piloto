from flask import Flask, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "/opt/piloto/data/permisos.csv"
LOG_FILE = "/opt/piloto/data/app.log"

# Asegurar que existan los archivos
os.makedirs("/opt/piloto/data", exist_ok=True)

# Crear CSV si no existe
if not os.path.isfile(DATA_FILE):
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "ticket", "fecha", "usuario", "accion",
            "grupo", "rol", "permisos", "proyecto", "responsable"
        ])


def log_event(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")


@app.route("/guardar", methods=["POST"])
def guardar():
    try:
        datos = [
            request.form.get("ticket"),
            request.form.get("fecha"),
            request.form.get("usuario"),
            request.form.get("accion"),
            request.form.get("grupo"),
            request.form.get("rol"),
            request.form.get("permisos"),
            request.form.get("proyecto"),
            request.form.get("responsable"),
        ]

        if not datos[0]:
            return "Falta ticket", 400

        with open(DATA_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(datos)

        log_event(f"Registro creado OK: {datos}")

        return "Registro guardado exitosamente"

    except Exception as e:
        log_event(f"ERROR: {str(e)}")
        return "Error en servidor", 500


@app.route("/")
def status():
    return "OK - Flask funcionando"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
