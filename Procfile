 web: cd ./web && python manage.py migrate && gunicorn --bind 0.0.0.0:80 --workers 3 web.wsgi:application