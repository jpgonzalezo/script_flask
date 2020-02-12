# Convertir cordenada (LATITUD, LONGITUD) en dirección
Programa que tiene la finalidad de tomar un conjunto de coordenadas en formato ( latitud , longitud ) y guardar 
en una nueva tabla las direcciones correspondientes a dichas coordenadas.

## Pre requisitos
1. Contar con una instalación limpia de python e inicializar un entorno virtual
2. Contar con acceso a la base de datos `nyg-batch-qa`

## Configuracion
1. Dentro del archivo `config.py` se encuentran los parametros de configuración para conectar la base de datos. 
Para ello debe modificarse la variable `SQLALCHEMY_DATABASE_URI` con los parametros que corresponda siguiendo la siguiente
estructura

`MOTOR_BASE_DATOS://USUARIO:CONTRASENNA@HOST:PORT/NOMBRE_BASE_DATOS`

2. Instalar las dependencias de python, ubicandose en la posiciónb raíz del proyecto y utilizando el comando `pip install requirements.txt`

3. Crear la donde se guardará las direcciones con ayuda del archivo `create_table.sql`

NOTA: Notesé que si modifica el nombre que lleva esta tabla, también deberá modificarlo en AddressLatLong bajo el parametro `address_lat_long`
ubicado en el archivo `location.py`

## Ejecución
1. Para ejecutar este script debe utilizar el comando `python script_update_lat_lng.py generateAddress`


