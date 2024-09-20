# Proyecto API de Estaciones

Este proyecto es una API desarrollada en Django que utiliza Docker y PostGIS para gestionar información sobre estaciones geográficas.

## Tecnologías utilizadas

- Django
- Django REST Framework
- PostGIS
- Docker

## Requisitos

Asegúrate de tener Docker y Docker Compose instalados en tu máquina.

## Configuración

1. Clona el repositorio:

   ```bash
   git clone https://github.com/luis-eduardo-caicedo/GeoStations.git
   ```

2. En la raíz del proyecto encontrarás un archivo llamado `env_example` que contiene un ejemplo de cómo debe estructurarse el archivo de variables de entorno. Usa este archivo como guía para crear tu propio archivo `.env` en la misma ubicación.

   Asegúrate de reemplazar los valores con los de tu entorno:

   ```env
   DATABASE_NAME=estaciones_db
   DATABASE_USER=admin
   DATABASE_PASSWORD=adminpassword
   SECRET_KEY=django-insecure-+3fpa!z6ca9jd=&5m@#zt%7@x%088o&wagtacjg#@3rfhwesw2
   ```

## Construcción y ejecución

Para construir el proyecto, primero ejecuta:

```bash
docker-compose build
```

Luego, corre las migraciones de la base de datos usando uno de los siguientes comandos:


```bash
docker-compose run web python manage.py migrate
```

Puedes crear un super usuario para el acceso al admin con el siguiente comando:


```bash
docker-compose run web python manage.py createsuperuser
```


Finalmente, inicia el contenedor:

```bash
docker-compose up
```

## Ejecución de pruebas

Para correr las pruebas del proyecto, puedes utilizar uno de los siguientes comandos:

```bash
docker-compose run web python manage.py test
```

## Uso de los Endpoints

La API ofrece los siguientes endpoints:

- **Listar estaciones**  
  `GET http://localhost:8000/api/station/list/`  
  Devuelve una lista de todas las estaciones.

- **Crear una nueva estación**  
  `POST http://localhost:8000/api/station/create/`  
  Crea una nueva estación.  
  **Body:**  
  ```json
  {
      "name": "Nombre de la estación",
      "ubication": "longitude,latitude"
  }
  ```

- **Listar estaciones cercanas**  
  `GET http://localhost:8000/api/station/near/<int:pk>/`  
  Devuelve una lista de estaciones cercanas a la ubicación especificada por el ID.

## Notas

Asegúrate de que los puertos utilizados no estén en uso por otros servicios en tu máquina.

- **Admin Django**  
  `GET http://localhost:8000/admin`  
