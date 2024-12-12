import requests
import pymongo
import schedule
import time
from datetime import datetime

# Conectar a MongoDB ejecutandose el contenedor docker llamado 'mongoBicis'
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
    print("No se pudo conectar a mongoDB.")
    exit(1)

# Función para obter los datos y guardarlos en la base de datos
def fetch_and_store_data():
    url = "http://api.citybik.es/v2/networks/bicicorunha"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un erro se a resposta non é exitosa
        data = response.json()

        # Engadimos a data e hora
        data['timestamp'] = datetime.now().isoformat()

        # Gardamos os datos en MongoDB
        collection.insert_one(data)
        print(f"Datos guardados correctamente en MongoDB: {data['timestamp']}")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar a API: {e}")
    except Exception as e:
        print(f"Error al guardar los datos en MongoDB: {e}")

# Programamos a execución a intervalos de 5 minutos
schedule.every(1).minutes.do(fetch_and_store_data)

# Mantemos o script en execución
try:
    while True:
        schedule.run_pending()  # Executa as tarefas programadas se é necesario
        time.sleep(1)  # Espera 1 segundo antes de comprobar de novo
except KeyboardInterrupt:
    # Aquí manejamos la desconexión manual
    print("\nDesconexión manual detectada.")