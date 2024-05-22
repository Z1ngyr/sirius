from django.apps import AppConfig
from django.db.models import CASCADE, ForeignKey


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    verbose_name = 'Jwt'