from flask import Flask, jsonify, request
from utils.database import get_postgresql_connection

app = Flask(__name__)

from flask import Flask, render_template, jsonify
from utils.database import get_postgresql_connection

app = Flask(__name__)

@app.route('/empleados', methods=['GET'])
def listar_empleados():
    conn = get_postgresql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, cargo FROM empleados;")
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([{"id": e[0], "nombre": e[1], "cargo": e[2]} for e in empleados]), 200

@app.route('/empleados/view', methods=['GET'])
def empleados_vista():
    return render_template('empleados.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
