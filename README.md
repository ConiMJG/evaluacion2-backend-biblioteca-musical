# 🎧 Mi Biblioteca Musical – Evaluación 2 (Backend)

Este proyecto es parte de la Evaluación 2 de la asignatura Backend.  
Consiste en una aplicación web desarrollada con **Django** que permite gestionar una biblioteca personal de canciones.

## 🚀 Funcionalidades

- Crear, leer, actualizar y eliminar canciones (CRUD completo)
- Visualización de calificación en estrellas ⭐
- Interfaz con navegación intuitiva
- Validación de datos como duración, calificación y año de lanzamiento

## 🧩 Modelo de datos

El modelo `Cancion` incluye:

- `titulo` (CharField)
- `artista` (CharField)
- `album` (CharField)
- `genero` (CharField)
- `duracion` (entero en segundos)
- `anio_lanzamiento` (entre 1900 y año actual)
- `calificacion` (1 a 5)
- `favorita` (booleano)
- `reproducciones` (entero, por defecto 0)

## 📸 Capturas

Puedes agregar capturas del sistema funcionando (opcional para entregar).

## ⚙️ Requisitos

- Python 3.8 o superior
- pip
- Entorno virtual (opcional pero recomendado)

## 📦 Instalación y ejecución

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/evaluacion2-backend-biblioteca-musical.git
cd evaluacion2-backend-biblioteca-musical

# Crear entorno virtual (opcional)
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar el servidor
python manage.py runserver
