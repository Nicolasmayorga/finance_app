# Django Finance App

Esta aplicación permite realizar el seguimiento de transacciones financieras y categorías de gastos. Proporciona una API para realizar operaciones CRUD en categorías y transacciones, así como un endpoint para obtener las categorías que han superado o no el presupuesto.

## Requisitos

- Python 3.6 o superior
- Django 3.2 o superior
- Django REST framework 3.12 o superior

## Configuración

1. Clona este repositorio en tu entorno local:


2. Navega hasta la carpeta del proyecto:


3. Instala las dependencias necesarias:

pip install -r requirements.txt


## Ejecución

1. Ejecuta las migraciones para configurar la base de datos:

python manage.py migrate


2. Inicia el servidor de desarrollo:

python manage.py runserver


La aplicación ahora debería estar ejecutándose en [http://localhost:8000/](http://localhost:8000/).

## Uso

La aplicación expone una API con los siguientes endpoints:

- Categorías:
  - Listar y crear: `/categories/`
  - Obtener, actualizar y eliminar: `/api/categories/<id>/`
- Transacciones:
  - Listar y crear: `/transactions/`
  - Obtener, actualizar y eliminar: `/transactions/<id>/`
- Categorías con estado de presupuesto:
  - Listar todas: `/budget_categories/`
  - Categorías que han superado el presupuesto: `/budget_categories/?search=True`
  - Categorías que no han superado el presupuesto: `/budget_categories/?search=False`

Puedes utilizar herramientas como [Postman](https://www.postman.com/) o [Curl](https://curl.se/) para probar y consumir la API.
