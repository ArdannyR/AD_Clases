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
    # Nota el cambio en la tabla: usamos DATE para la fecha
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            descripcion TEXT,
            estado VARCHAR(50) DEFAULT 'Pendiente',
            fecha_limite DATE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla 'tareas' verificada/creada correctamente.")

# --- READ Y FILTRAR ---
@app.route("/")
def index():
    # Capturamos si el usuario envió un filtro por la URL (?estado=...)
    estado_filtro = request.args.get("estado")
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    if estado_filtro and estado_filtro != "Todos":
        cursor.execute("SELECT * FROM tareas WHERE estado = %s", (estado_filtro,))
    else:
        cursor.execute("SELECT * FROM tareas")
        
    tareas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", tareas=tareas, nodo=db_host, filtro_actual=estado_filtro)

# --- CREATE ---
@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form["titulo"]
    descripcion = request.form["descripcion"]
    estado = request.form["estado"]
    fecha_limite = request.form["fecha_limite"]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tareas (titulo, descripcion, estado, fecha_limite) VALUES (%s, %s, %s, %s)",
        (titulo, descripcion, estado, fecha_limite)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

# --- UPDATE ---
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    nuevo_estado = request.form["nuevo_estado"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tareas SET estado = %s WHERE id = %s",
        (nuevo_estado, id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

# --- DELETE ---
@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)