import sqlite3

conexion = sqlite3.connect("citas.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mascota TEXT NOT NULL,
    propietario TEXT NOT NULL,
    especie TEXT,
    fecha TEXT NOT NULL
)
""")

conexion.commit()
conexion.close()

print("Base de datos y tabla creadas correctamente.")