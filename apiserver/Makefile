apiserver.prod:
	gunicorn -w 4 -k gevent "apiserver.wsgi"

apiserver.local:
	python3 manage.py runserver

