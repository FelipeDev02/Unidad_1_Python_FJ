Primer proyecto de backend

python -m venv env

source env/Scripts/activate

pip install django

python manage.py runserver


para guardar cambios en los modelos:

python manage.py makemigrations

python manage.py migrate

Si no configuramos una base de datos externa, Django usa SQLite por defecto y guarda todo en el archivo db.sqlite3. Así podemos empezar rápido sin instalar un motor como MySQL o PostgreSQL.

Probando modelos guardados en la shell

python manage.py shell => abriendo una shell dentro de la shell


from dispositivos.models import Dispositivo => importando el modelo
Dispositivo.objects.create(nombre='Sensor Temp', consumo=50, estado=True) => creando un objeto
Dispositivo.objects.all() => Mostrando objetos creados desde Dispositivo.

superuser = admin
psswd = admin123
