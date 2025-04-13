# TuPrimeraPaginaLUNA

Este es mi primer proyecto web con Django. Se trata de un blog simple que permite administrar autores, categorías y posts. También se puede buscar contenido por palabras clave.

## 🧱 Estructura del proyecto

- Utiliza el patrón MVT (Model-View-Template).
- Se implementó herencia de plantillas con `base.html`.
- Se crearon 3 modelos: `Autor`, `Categoria` y `Post`.
- Formularios para crear datos de cada modelo.
- Formulario de búsqueda por título o contenido de los posts.

## 🚀 Cómo probar la app

### 1. Cloná el repositorio

```bash
git clone https://github.com/LautaroLuna/TuPrimeraPaginaLUNA.git
cd TuPrimeraPaginaLUNA

### 2. Crear entorno virtual (opcional pero recomendado)

python -m venv env
env\Scripts\activate   # En Windows

### 3. Instalá dependencias

pip install django

### 4. Aplicá las migraciones y creá superusuario

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5. Iniciá el servidor

python manage.py runserver

🧪 ¿Qué funcionalidades probar?
🌐 Inicio
Ir a: http://127.0.0.1:8000/
Muestra una página de bienvenida.

➕ Crear contenido
Ir a:

/nuevo_autor/ para agregar un autor

/nueva_categoria/ para agregar una categoría

/nuevo_post/ para agregar un post (requiere autor y categoría creados)

🔍 Buscar contenido
Ir a:

/buscar_post/ y escribir parte del título o contenido de un post

🛠 Administrar desde el panel de Django
Ir a:

/admin/ e iniciar sesión con tu superusuario

Como es la estructura de mis 📁carpetas:

TuPrimeraPaginaLUNA/
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── inicio.html
│           ├── nuevo_autor.html
│           ├── nueva_categoria.html
│           ├── nuevo_post.html
│           └── buscar_post.html
├── manage.py
└── README.md

👤 Autor
Lautaro Luna
https://github.com/LautaroLuna