import os
import time
from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

db_host = os.environ.get("DB_HOST", "mysql_principal")

def get_connection():
    retries = 10
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host=db_host,
                user="root",
                password="root",
                database="replica"
            )
            return conn
        except Error as e:
            print(f"[{i+1}/{retries}] Esperando MySQL en {db_host}... {e}")
            time.sleep(3)
    raise Exception(f"No se pudo conectar a MySQL en {db_host}")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peliculas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            genero VARCHAR(100),
            anio INT,
            director VARCHAR(255)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla 'peliculas' verificada/creada correctamente.")

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", peliculas=peliculas, nodo=db_host)

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    anio = request.form["anio"]
    director = request.form["director"]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO peliculas (titulo, genero, anio, director) VALUES (%s, %s, %s, %s)",
        (titulo, genero, anio, director)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)