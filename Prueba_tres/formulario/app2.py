from flask import Flask, render_template, request, redirect
import mysql.connector
import time
import os

app = Flask(__name__)
db_host = os.environ.get("DB_HOST", "mysql_principal")

def obtener_conexion():
    retries = 5
    while retries > 0:
        try:
            conexion = mysql.connector.connect(
                host=db_host,
                user="root",
                password="root",
                database="replica"
            )
            return conexion
        except mysql.connector.Error as err:
            print(f"Base de datos no lista ({err}). Reintentando en 5 segundos...")
            retries -= 1
            time.sleep(5)
            
    raise Exception("No se pudo conectar a la base de datos después de varios intentos.")


@app.route("/")
def index():
    return render_template("index.html", nodo=db_host)
   
@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    formacion = request.form["formacion"]
    experiencia = request.form["experiencia"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute(
        "INSERT INTO informacion (nombre, correo, formacion, experiencia) VALUES (%s, %s, %s, %s)",
        (nombre, correo, formacion, experiencia)
    )
    conexion.commit() # Guarda permanentemente los cambios
    
    cursor.close()
    conexion.close() # Cierra la conexión, muy importante en aplicaciones web

    return redirect("/") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)