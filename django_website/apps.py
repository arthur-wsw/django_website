from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "django_website"

    def ready(self):
        import_module("django_website.receivers")
