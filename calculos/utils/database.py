import psycopg2
from pymongo import MongoClient
import os

# Conexión a PostgreSQL
def get_postgresql_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "cobros_db"),
        user=os.getenv("POSTGRES_USER", "cobros_user"),
        password=os.getenv("POSTGRES_PASSWORD", "cobros_password"),
        host=os.getenv("POSTGRES_HOST", "10.128.0.82"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )

# Conexión a MongoDB
def get_mongo_connection():
    client = MongoClient(
        os.getenv("MONGO_URI", "mongodb://mongo_user:mongo_password@10.128.0.83:27017/")
    )
    db = client[os.getenv("MONGO_DB", "nombre_base_mongo")]
    return db

