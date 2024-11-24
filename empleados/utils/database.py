import psycopg2
import os

def get_postgresql_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "app_db"),
        user=os.getenv("POSTGRES_USER", "app_user"),
        password=os.getenv("POSTGRES_PASSWORD", "app_password"),
        host=os.getenv("POSTGRES_HOST", "10.128.0.82"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )
