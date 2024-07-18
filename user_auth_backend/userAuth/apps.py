from django.apps import AppConfig


class UserauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userAuth'

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals
