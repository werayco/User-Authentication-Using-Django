from django.apps import AppConfig


class AccntRegConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accnt_reg"

    def ready(self):
        import accnt_reg.signals


