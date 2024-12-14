# Proyecto de Integración con API y MongoDB

Este proyecto consta de dos scripts que interactúan con una API, almacenan los datos en una base de datos MongoDB y permiten exportar los datos en diferentes formatos. A continuación se detalla cómo ejecutar y utilizar cada uno de los scripts.
## Carpetas
- Ejercicio básico
  -Este ejercicio contiene los primeros puntos del trabajo 
- Ejercicio avanzado
  -Este ejercicio contiene el ejercicio básico pero se ha creado una network y un docker compose en el que crean 2 contenedores.   
- Ejercicio noticias
  -En este ejercicio hacemos lo mismo que el ejercicio básico pero con una API distinta 

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

## Conclusión
Este ejercicio de integración con una API y almacenamiento de datos en MongoDB ha proporcionado una comprensión práctica de cómo interactuar con una API, procesar los datos obtenidos y almacenarlos en una base de datos MongoDB.


# Ejercicio avanzado

Una vez en la carpeta avanzado Para dockerizar este script, utiliza el archivo Dockerfile incluido en el proyecto.

### Construcción de la Imagen Docker
Ejecuta el siguiente comando en la terminal para construir la imagen Docker:

> docker build -t conexionapi .

El archivo docker-compose.yml está configurado para iniciar un contenedor que ejecuta un servidor MongoDB. Para levantar el servidor, utiliza el siguiente comando:

> docker-compose up -d

Una vez que el servidor MongoDB esté en funcionamiento, puedes utilizar el script exportarDataframe.py, ubicado en la carpeta scripts, para realizar la exportación de datos.
Ejecuta el siguiente comando para ejecutar el script:

> python script2.py

## Conclusión

En este ejercicio he aprendido a:

1. Crear y configurar un Dockerfile para dockerizar un script de Python.

2. Utilizar docker-compose para configurar un servidor MongoDB.

3.Integrar el uso de contenedores con scripts de Python para realizar tareas automatizadas.

