# Proyecto de Integración con API y MongoDB

Este proyecto consta de dos scripts que interactúan con una API, almacenan los datos en una base de datos MongoDB y permiten exportar los datos en diferentes formatos. A continuación se detalla cómo ejecutar y utilizar cada uno de los scripts.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- MongoDB en ejecución
- Docker desktop
  
- Las siguientes bibliotecas de Python:
  - `requests`
  - `pymongo`
  - `pandas`
  - `pyarrow` (para trabajar con el formato Parquet)


Puedes instalar las dependencias con el siguiente comando:

> pip install requests pymongo pandas pyarrow

## En docker desktop puedes crear el docker de mongoBD para poder trabajar:
Debes crear un docker con la imagen de mongo:  mongo docker run --name mongoBicis -d -p 27017:27017 mongo

## Script 1: Obtención y almacenamiento de datos en MongoDB
## conexionAPI.py
Este script se conecta a una API a intervalos regulares (por defecto, cada 1 minutos) y almacena los datos obtenidos en una base de datos MongoDB. La ejecución del script continuará indefinidamente hasta que se cancele manualmente.
#### Ejecución: Para ejecutar el script, simplemente corre el siguiente comando en tu terminal:


> python script1.py

El script comenzará a obtener los datos de la API y a almacenarlos en la base de datos MongoDB de forma continua.

## Script 2: Lectura y exportación de datos desde MongoDB
## exportarDataframe.py
Este script lee los datos almacenados en MongoDB y los carga en un dataframe de Pandas. Luego, permite exportar los datos en los formatos CSV y Parquet. El script se ejecuta por demanda, lo que significa que puedes correrlo en cualquier momento para obtener los datos.
#### Ejecución: Para ejecutar el script y exportar los datos a los formatos solicitados, usa el siguiente comando:


> python script2.py

El script:

- `Lee los datos de la base de datos MongoDB.`
- `Extrae solo los campos necesarios: id, name, timestamp, free_bikes, empty_slots, uid, last_updated, slots, normal_bikes, ebikes.`
- `Exporta los datos en formato CSV y Parquet en el directorio donde se ejecuta el script.`

Formatos de exportación:
CSV: Los datos se exportarán a un archivo .csv.
Parquet: Los datos se exportarán a un archivo .parquet.
