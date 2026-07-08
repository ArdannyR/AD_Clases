from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_FILE = os.environ.get("DB_PATH", "asistencia.db")

def init_db():
    db_dir = os.path.dirname(DB_FILE)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS asistentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL,
                evento TEXT NOT NULL
            )
        ''')
        conn.commit()
        
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        evento = request.form.get('evento')
        
        if nombre and email and evento:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO asistentes (nombre, email, evento) VALUES (?, ?, ?)", 
                               (nombre, email, evento))
                conn.commit()
        return redirect('/')
    
    # Renderizar para GET
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asistentes ORDER BY id DESC LIMIT 5")
        registros = cursor.fetchall()
        
    return render_template('index.html', registros=registros)

if __name__ == '__main__':
    # Ejecutamos en modo multihilo para soportar pruebas de carga concurrentes si se corre localmente
    app.run(host='0.0.0.0', port=5000, threaded=True)
