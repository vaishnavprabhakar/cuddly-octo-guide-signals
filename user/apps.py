from django.apps import AppConfig
import threading

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self) -> None:
        import user.signals
