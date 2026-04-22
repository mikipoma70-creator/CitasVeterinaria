from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("citas.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    pacientes = conn.execute("SELECT * FROM pacientes").fetchall()
    conn.close()
    return render_template("index.html", pacientes=pacientes)

@app.route("/agendar", methods=["GET", "POST"])
def agendar():
    if request.method == "POST":
        mascota = request.form["mascota"]
        propietario = request.form["propietario"]
        especie = request.form["especie"]
        fecha = request.form["fecha"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO pacientes (mascota, propietario, especie, fecha) VALUES (?, ?, ?, ?)",
            (mascota, propietario, especie, fecha)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("agendar.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = get_db_connection()
    paciente = conn.execute("SELECT * FROM pacientes WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        mascota = request.form["mascota"]
        propietario = request.form["propietario"]
        especie = request.form["especie"]
        fecha = request.form["fecha"]

        conn.execute(
            "UPDATE pacientes SET mascota = ?, propietario = ?, especie = ?, fecha = ? WHERE id = ?",
            (mascota, propietario, especie, fecha, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn.close()
    return render_template("editar.html", paciente=paciente)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM pacientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)