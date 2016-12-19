python manage.py makemigrations
python manage.py migrate
gunicorn ebyokola.wsgi --log-file -