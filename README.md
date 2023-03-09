# Prueba de nivel para Teknei

Aplicación para listar libros.

La aplicación incorpora paginación y validación de formularios.

Las siguientes instrucciones son aplicables a plataformas Linux y MacOS.

Para ejecutar la aplicación por primera vez, primero hay que crear un entorno virtual.
```bash
python -m venv venv
```

Clonar el repositorio.
```bash
git clone https://github.com/BenjaminPina/teknei.git
```

Cambiar al directorio donde se encuentra el código.
```bash
cd teknei
```

Instalar los requerimientos.
```bash
pip install -r requirements.txt
```

El proyecto se encuentra configurado para trabajar con base de datos SQLite.
Para inicializar la base de datos solamente es necesario aplicar las migraciones.
```bash
python manage.py migrate
```

Crear el súper usuario. Ejecutar el siguiente comando y seguir instrucciones.
```bash
python manage.py createsuperuser
```

De ahora en adelante el proyecto se podrá ejecutar activando el entorno virtual (si es que no está activo)
y levantando el servidor de desarrollo.
```bash
python manage.py runserver
```

En caso de que el entorno virtual no esté activo, desde la carpeta que contenga los
directorios venv/ y teknei/ se ejecutan los siguientes comandos.
```bash
source venv/bin/activate
cd teknei
python manage.py runserver
```

Una vez levantado el servidor de desarrollo se puede acceder a la aplicación desde
el navegador local mediante la siguiente URL:

http://localhost:8000/


También se puede acceder con las credenciales de súper usuario al administrador de Django desde la siguiente URL:

http://localhost:8000/admin/