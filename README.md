# --SESSION 1
## USUARIO  GIT
git config user.name
git config user.email

## INSTALAR
python -m venv .venv
pip install django
## VER TUS INSTALACIONES DENTRO DE (.venv)
pip list
python -m pip freeze > requirements.txt

## CREAR PROYECTO
django-admin startproject webproductos
## EJECUTAR EN EL SERVIDOR
python manage.py runserver
python manage.py runserver 7000
## CREAR APP
python manage.py startapp productos
## MIGRAR TABLAS
python manage.py migrate
## SUPERUSUARIO
python manage.py createsuperuser
# levanta la web
http://127.0.0.1:8000/admin/login/?next=/admin/
# crear usuario (luego haz pruebas de permisos del usuario)
http://127.0.0.1:8000/admin/auth/user/add/
http://127.0.0.1:8000/admin/core/detalle/3/change/
es: piero | 3strell4_41.$$

## INSTALLED_APPS
agregar 'core',
## CREAR APP
python manage.py startapp core
## TRABAJR CON ImageField
pip install pillow
## MIGRAR TUS PROPIAS TABLAS
python manage.py makemigrations core
python manage.py migrate (confirmar cambios admin)
## LUEGO
tevas a admin.py y lo agregas para verlo en django admin




# --SESSION 2
## MIGRA SQLite a POSTGRESQL
pip install psycopg2-binary
Crea tu bd en postgress

## CONFIGURA DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bdcomercial',
        'USER': 'postgres',
        'PASSWORD': '47736559',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


## PASOS
Elimina la carpeta migrations (configuracion de sqlLite)
regresa a la carpeta raiz de tu proyecto 
vuelves a levantar el .venv
escribes: python manage.py makemigrations core
Mostrar: Migrations for 'core': , y s evolvio a crear la carpeta migration
escribes: python manage.py migrate (migrar tablas a postgresql)

## SUPERUSUARIO
python manage.py createsuperuser (crear user, email , pass)
python manage.py runserver (prueba iniciando session)
