from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'Account'

    def ready(self):
        import users.signals
