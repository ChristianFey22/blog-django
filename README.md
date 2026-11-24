# Blog Django

Proyecto de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene un proyecto Django para construir un blog inmobiliario.
Incluye la configuración base del proyecto y una aplicación llamada `posts`, que ya cuenta con
vistas basadas en funciones, templates con herencia y archivos estáticos (CSS).

El flujo implementado es: **ruta -> vista -> template -> estático**.

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

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Páginas del sitio

| URL | Descripción |
|---|---|
| `/` | Página de inicio |
| `/acerca/` | Página "Acerca de" |

El menú de navegación está definido en `base.html` y permite moverse entre ambas páginas.

## Aplicaciones

- `posts`: aplicación para manejar las publicaciones del blog. Por ahora contiene las páginas de inicio y "Acerca de".

### Estructura de la app `posts`

```
posts/
├── templates/posts/
│   ├── base.html        (layout base con menú y bloque de contenido)
│   ├── inicio.html      (página de inicio)
│   └── acerca.html      (página "Acerca de")
├── static/posts/css/
│   └── estilos.css      (estilos del sitio)
├── urls.py              (rutas de la app)
└── views.py             (vistas basadas en funciones)
```

Las rutas de la app se conectan al proyecto desde `blog_project/urls.py` mediante `include()`.
