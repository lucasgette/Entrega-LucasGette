# RaveReviews sitio web

## Configuración

En primer lugar, será necesario clonar el repositorio:

```sh
$ git clone https://github.com/lucasgette/Entrega1-Gette.git

```

Crear y activar un ambiente virtual en el cual instalaremos los paquetes necesarios para el proyecto:

```sh
$ py -m venv venv
$ . venv/scripts/activate
```

Estando activado el entorno virtual creado, instalar los paquetes necesarios a partir de requirements.txt:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` en la terminal nos indicará que está operando en el entorno virtual que hemos creado y denominado venv


Una vez que `pip` haya descargado e instalado los paquetes, podemos hacer correr el servidor:
```sh
(venv)$ python manage.py runserver
```


## Navegar el sitio y conocer sus funcionalidades

El sitio cuenta con una página de inicio, en la que podemos ver 3 tarjetas con las 3 secciones principales del sitio:
* Peliculas
* Series
* Libros

En cada una de esas secciones, podremos acceder 
