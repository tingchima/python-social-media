import os

from celery import Celery

# ref. https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#django-first-steps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.base")

app = Celery("python-social-media")


app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(name="debug task", bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
