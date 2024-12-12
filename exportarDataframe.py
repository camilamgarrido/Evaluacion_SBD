import pandas as pd
import pymongo

# Conexión a MongoDB
def get_mongo_client():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión con MongoDB: {e}")
        return None

# Intentar reconectar si no hay conexión
client = get_mongo_client()
if client:
    db = client["bicicorunha_db"]
    collection = db["data"]
else:
    print("No se pudo conectar a MongoDB.")
    exit(1)

# Leer datos desde MongoDB y exportar
try:
    # Leer datos desde MongoDB
    documents = collection.find()

    # Transformar los documentos en una lista de diccionarios
    data = []
    for doc in documents:
        for station in doc['network']['stations']:
            data.append({
                "id": station.get("id"),
                "name": station.get("name"),
                "timestamp": doc.get("timestamp"),
                "free_bikes": station.get("free_bikes"),
                "empty_slots": station.get("empty_slots"),
                "uid": station.get("extra", {}).get("uid"),
                "last_updated": station.get("extra", {}).get("last_updated"),
                "slots": station.get("extra", {}).get("slots"),
                "normal_bikes": station.get("extra", {}).get("normal_bikes"),
                "ebikes": station.get("extra", {}).get("ebikes")
            })

    # Crear el DataFrame
    df = pd.DataFrame(data)

    if not df.empty:
        # Exportar a CSV
        csv_filename = "bicicorunha_data.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Datos exportados correctamente a {csv_filename}")

        # Exportar a Parquet
        parquet_filename = "bicicorunha_data.parquet"
        df.to_parquet(parquet_filename, index=False)
        print(f"Datos exportados correctamente a {parquet_filename}")
    else:
        print("No se encontraron datos para exportar.")

except Exception as e:
    print(f"Error al procesar los datos: {e}")