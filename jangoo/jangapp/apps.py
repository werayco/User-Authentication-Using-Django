from django.apps import AppConfig


class JangappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "jangapp"

    def ready(self):
        import jangapp.signals
