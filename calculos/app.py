from flask import Flask, jsonify
from utils.database import get_mongo_connection
from pymongo.errors import PyMongoError

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def obtener_suma():
    try:
        db = get_mongo_connection()
        collection = db['suma_total']
        suma_total = collection.find_one({"_id": "suma_total"})

        # Si no se encuentra el documento, devolver 0 como suma total
        if suma_total:
            return jsonify({"suma_total": suma_total['suma_total']}), 200
        else:
            return jsonify({"suma_total": 0}), 200
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

