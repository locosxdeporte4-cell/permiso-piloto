from flask import Flask, request
import csv
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "/opt/piloto/data/permisos.csv"

@app.route("/guardar", methods=["POST"])
def guardar():
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

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(datos)

    return "Permiso registrado correctamente"

@app.route("/")
def home():
    return "La aplicación Flask está corriendo. Ir a /index.html para el formulario."

app.run(host="0.0.0.0", port=5000)
