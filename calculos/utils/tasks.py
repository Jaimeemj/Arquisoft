from utils.database import get_postgresql_connection, get_mongo_connection
from decimal import Decimal


# Calcular promedio de cobros pagados
def calcular_promedio_pagados():
    conn = get_postgresql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(monto) FROM cobros_cobro WHERE pagado = TRUE;")
    promedio = cursor.fetchone()[0] or 0
    cursor.close()
    conn.close()
    return promedio
    

# Actualizar promedio en MongoDB
def actualizar_promedio_mongo():
    promedio = calcular_promedio_pagados()
    promedio = float(promedio) if isinstance(promedio, Decimal) else promedio
    db = get_mongo_connection()
    collection = db['promedios']
    collection.update_one(
        {"_id": "promedio_pagados"},
        {"$set": {"promedio_pagados": promedio}},
        upsert=True
    )
    