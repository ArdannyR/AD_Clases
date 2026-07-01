import hashlib
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import requests
from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave-docente-cambiar")

ENDPOINT_URL = os.getenv(
    "ENDPOINT_URL", "http://172.31.118.15:3000/selecciones"
)
DB_PATH = os.getenv("DB_PATH", "/app/data/selecciones.db")
DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"


def ahora_iso() -> str:
    """Fecha y hora UTC en formato legible y estable."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def conexion() -> sqlite3.Connection:
    """Abre la base SQLite y permite leer columnas por nombre."""
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def inicializar_bd() -> None:
    """Crea la tabla si todavía no existe."""
    with conexion() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS selecciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                remote_key TEXT UNIQUE,
                nombre TEXT NOT NULL,
                continente TEXT NOT NULL DEFAULT '',
                grupo TEXT NOT NULL DEFAULT '',
                origen TEXT NOT NULL DEFAULT 'local',
                actualizado_en TEXT NOT NULL
            )
            """
        )


def extraer_lista(payload):
    """Admite una lista directa o una lista contenida en una clave común."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for clave in ("selecciones", "data", "results", "items"):
            valor = payload.get(clave)
            if isinstance(valor, list):
                return valor
        return [payload]
    raise ValueError("El endpoint no devolvió una lista ni un objeto JSON válido.")


def primer_valor(item: dict, claves: tuple[str, ...], predeterminado=""):
    for clave in claves:
        valor = item.get(clave)
        if valor is not None and str(valor).strip():
            return str(valor).strip()
    return predeterminado


def normalizar_item(item, posicion: int) -> dict:
    """Convierte distintos nombres de campos a un formato común."""
    if not isinstance(item, dict):
        item = {"nombre": str(item)}

    identificador = primer_valor(item, ("id", "_id", "codigo", "code"))
    nombre = primer_valor(
        item,
        ("nombre", "seleccion", "pais", "name", "equipo", "team"),
        f"Selección {posicion}",
    )
    continente = primer_valor(item, ("continente", "confederacion", "region"))
    grupo = primer_valor(item, ("grupo", "group"))

    if identificador:
        remote_key = f"id:{identificador}"
    else:
        base = json.dumps(item, sort_keys=True, ensure_ascii=False)
        remote_key = "hash:" + hashlib.sha256(base.encode("utf-8")).hexdigest()[:20]

    return {
        "remote_key": remote_key,
        "nombre": nombre,
        "continente": continente,
        "grupo": grupo,
    }


def obtener_datos_fuente():
    """Consulta el endpoint real o, solo como contingencia, datos de demostración."""
    if DEMO_MODE:
        ruta_demo = Path(__file__).with_name("demo_data.json")
        return json.loads(ruta_demo.read_text(encoding="utf-8")), "demostración"

    respuesta = requests.get(ENDPOINT_URL, timeout=12)
    respuesta.raise_for_status()
    return respuesta.json(), "endpoint"


def sincronizar() -> int:
    """Importa o actualiza en SQLite la información recibida."""
    payload, origen_fuente = obtener_datos_fuente()
    elementos = extraer_lista(payload)
    contador = 0

    with conexion() as db:
        for posicion, item in enumerate(elementos, start=1):
            seleccion = normalizar_item(item, posicion)
            db.execute(
                """
                INSERT INTO selecciones
                    (remote_key, nombre, continente, grupo, origen, actualizado_en)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(remote_key) DO UPDATE SET
                    nombre = excluded.nombre,
                    continente = excluded.continente,
                    grupo = excluded.grupo,
                    origen = excluded.origen,
                    actualizado_en = excluded.actualizado_en
                """,
                (
                    seleccion["remote_key"],
                    seleccion["nombre"],
                    seleccion["continente"],
                    seleccion["grupo"],
                    origen_fuente,
                    ahora_iso(),
                ),
            )
            contador += 1
    return contador


@app.get("/")
def inicio():
    with conexion() as db:
        selecciones = db.execute(
            "SELECT * FROM selecciones ORDER BY nombre COLLATE NOCASE"
        ).fetchall()
    return render_template(
        "index.html",
        selecciones=selecciones,
        endpoint_url=ENDPOINT_URL,
        demo_mode=DEMO_MODE,
    )


@app.post("/sincronizar")
def sincronizar_ruta():
    try:
        cantidad = sincronizar()
        flash(f"Sincronización completada: {cantidad} registro(s) procesado(s).", "ok")
    except requests.RequestException as error:
        flash(
            "No se pudo consultar el endpoint. Verifique la red, VPN o dirección. "
            f"Detalle: {error}",
            "error",
        )
    except (ValueError, json.JSONDecodeError) as error:
        flash(f"La respuesta recibida no pudo procesarse: {error}", "error")
    return redirect(url_for("inicio"))


@app.post("/nueva")
def nueva():
    nombre = request.form.get("nombre", "").strip()
    continente = request.form.get("continente", "").strip()
    grupo = request.form.get("grupo", "").strip()

    if not nombre:
        flash("El nombre de la selección es obligatorio.", "error")
        return redirect(url_for("inicio"))

    with conexion() as db:
        db.execute(
            """
            INSERT INTO selecciones
                (remote_key, nombre, continente, grupo, origen, actualizado_en)
            VALUES (NULL, ?, ?, ?, 'local', ?)
            """,
            (nombre, continente, grupo, ahora_iso()),
        )
    flash("Nueva selección guardada localmente.", "ok")
    return redirect(url_for("inicio"))


@app.route("/editar/<int:seleccion_id>", methods=["GET", "POST"])
def editar(seleccion_id: int):
    with conexion() as db:
        seleccion = db.execute(
            "SELECT * FROM selecciones WHERE id = ?", (seleccion_id,)
        ).fetchone()

        if seleccion is None:
            flash("La selección solicitada no existe.", "error")
            return redirect(url_for("inicio"))

        if request.method == "POST":
            nombre = request.form.get("nombre", "").strip()
            continente = request.form.get("continente", "").strip()
            grupo = request.form.get("grupo", "").strip()

            if not nombre:
                flash("El nombre no puede quedar vacío.", "error")
                return render_template("editar.html", seleccion=seleccion)

            db.execute(
                """
                UPDATE selecciones
                SET nombre = ?, continente = ?, grupo = ?,
                    origen = 'local-editado', actualizado_en = ?
                WHERE id = ?
                """,
                (nombre, continente, grupo, ahora_iso(), seleccion_id),
            )
            flash("Selección actualizada y guardada.", "ok")
            return redirect(url_for("inicio"))

    return render_template("editar.html", seleccion=seleccion)


@app.get("/api/selecciones")
def api_selecciones():
    with conexion() as db:
        filas = db.execute(
            "SELECT id, nombre, continente, grupo, origen, actualizado_en "
            "FROM selecciones ORDER BY nombre COLLATE NOCASE"
        ).fetchall()
    return jsonify([dict(fila) for fila in filas])

@app.get("/api/resumen")
def api_resumen():
    with conexion() as db:
        total = db.execute("SELECT COUNT(*) FROM selecciones").fetchone()[0]
        filas_origen = db.execute(
            "SELECT origen, COUNT(*) as cantidad FROM selecciones GROUP BY origen"
        ).fetchall()
        detalle_origen = {fila["origen"]: fila["cantidad"] for fila in filas_origen}

    return jsonify({
        "total": total,
        "por_origen": detalle_origen
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "service": "taller-semana-13"})


inicializar_bd()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
