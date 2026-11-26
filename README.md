# Blog Django

Proyecto de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene un proyecto Django para construir un blog inmobiliario.
Incluye la configuración base del proyecto y una aplicación llamada `posts`, con vistas basadas en funciones,
templates con herencia, archivos estáticos (CSS) y un modelo `Post` guardado en una base de datos SQLite.

Las publicaciones se cargan desde el panel de administración de Django y se muestran en el sitio
consultando la base de datos con el ORM.

El flujo implementado es: **ruta -> vista -> (ORM) -> template -> estático**.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/ChristianFey22/blog-django.git
```

Entrar a la carpeta del proyecto:

```bash
cd blog-django
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual:

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear la base de datos local aplicando las migraciones:

```bash
python manage.py migrate
```

> El archivo `db.sqlite3` no se sube al repositorio. Se genera en cada computadora al ejecutar `migrate`.

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Panel de administración

Las publicaciones se gestionan desde el panel de administración de Django.

1. Crear un superusuario (solo la primera vez):

```bash
python manage.py createsuperuser
```

Django pide un nombre de usuario, un email y una contraseña. Al escribir la contraseña la terminal no muestra caracteres.

2. Con el servidor en ejecución, abrir:

http://127.0.0.1:8000/admin/

3. Iniciar sesión con el superusuario y entrar en la sección **Posts** para crear, editar o eliminar publicaciones.

En el listado del admin se muestran el título, el autor, la fecha de creación y el estado de cada post, y se puede buscar y filtrar por estado.

## Modelo `Post`

| Campo | Tipo | Descripción |
|---|---|---|
| `titulo` | `CharField` | Título de la publicación |
| `contenido` | `TextField` | Contenido completo |
| `autor` | `CharField` | Nombre del autor |
| `fecha_creacion` | `DateTimeField` | Se completa automáticamente al crear el post |
| `estado` | `CharField` | `borrador`, `publicado` o `archivado` |

Solo los posts con estado `publicado` se muestran en el sitio.

## Páginas del sitio

| URL | Descripción |
|---|---|
| `/` | Página de inicio |
| `/acerca/` | Página "Acerca de" |
| `/posts/` | Listado de posts publicados, cargados desde la base de datos |
| `/admin/` | Panel de administración (requiere superusuario) |

El menú de navegación está definido en `base.html` y permite moverse entre las páginas públicas.

## Aplicaciones

- `posts`: aplicación para manejar las publicaciones del blog.

### Estructura de la app `posts`

```
posts/
├── migrations/          (historial de cambios del modelo)
├── templates/posts/
│   ├── base.html        (layout base con menú y bloque de contenido)
│   ├── inicio.html      (página de inicio)
│   ├── acerca.html      (página "Acerca de")
│   └── lista_posts.html (listado de posts publicados)
├── static/posts/css/
│   └── estilos.css      (estilos del sitio)
├── admin.py             (configuración del panel de administración)
├── models.py            (modelo Post)
├── urls.py              (rutas de la app)
└── views.py             (vistas basadas en funciones)
```

Las rutas de la app se conectan al proyecto desde `blog_project/urls.py` mediante `include()`.