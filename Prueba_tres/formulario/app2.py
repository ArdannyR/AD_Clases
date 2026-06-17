from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conexion = mysql.connector.connect(
    host="mysql_principal",
    user="root",
    password="root",
    database="replica"
)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    formacion = request.form["formacion"]
    experiencia = request.form["experiencia"]

    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO replica (nombre, correo, formacion,experiencia) VALUES (%s, %s, %s,%s)",
        (nombre, correo, formacion,experiencia)
    )
    conexion.commit() # Guarda permanentemente los cambios realizados en la base de datos.

    return redirect("/") #envía al navegador nuevamente a la ruta principal

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

