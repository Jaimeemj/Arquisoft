from utils.database import get_postgresql_connection, get_mongo_connection
import psycopg2
from pymongo.errors import PyMongoError

def calcular_suma_postgresql():
    try:
        conn = get_postgresql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(monto) FROM cobros;")
        suma = cursor.fetchone()[0] or 0
        cursor.close()
        conn.close()
        return suma
    except psycopg2.Error as e:
        print(f"Error al calcular la suma en PostgreSQL: {e}")
        return 0

def actualizar_suma_mongo():
    try:
        suma_total = calcular_suma_postgresql()
        db = get_mongo_connection()
        collection = db['suma_total']
        collection.update_one(
            {"_id": "suma_total"},
            {"$set": {"suma_total": suma_total}},
            upsert=True
        )
    except PyMongoError as e:
        print(f"Error al actualizar MongoDB: {e}")
