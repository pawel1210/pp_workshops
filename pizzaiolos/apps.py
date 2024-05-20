from django.apps import AppConfig


class PizzaiolosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pizzaiolos'

    def ready(self):
        import pizzaiolos.signals
