import os
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_host = os.environ.get("DB_HOST", "mysql_principal")

conexion = mysql.connector.connect(
    host="mysql_principal",
    user="root",
    password="root",
    database="replica"
)

@app.route("/")
def index():
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()
    return render_template("index.html", peliculas=peliculas)

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    anio = request.form["anio"]
    director = request.form["director"]

    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO peliculas (titulo, genero, anio, director) VALUES (%s, %s, %s, %s)",
        (titulo, genero, anio, director)
    )
    conexion.commit() # Guarda permanentemente los cambios realizados en la base de datos.

    return redirect("/") #envía al navegador nuevamente a la ruta principal

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)