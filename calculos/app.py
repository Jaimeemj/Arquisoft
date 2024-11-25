from flask import Flask, jsonify
from utils.database import get_mongo_connection


app = Flask(__name__)

@app.route('/promedio', methods=['GET'])
def obtener_promedio():
    db = get_mongo_connection()
    collection = db['promedios']
    promedio_doc = collection.find_one({"_id": "promedio_pagados"})

    # Si no se encuentra el documento, devolver 0 como promedio
    if promedio_doc:
        return jsonify({"promedio_pagados": promedio_doc['promedio_pagados']}), 200
    else:
        return jsonify({"promedio_pagados": 0}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

