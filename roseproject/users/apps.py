from django.apps import AppConfig
from .signals import

class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals