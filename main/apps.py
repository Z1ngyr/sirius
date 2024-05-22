from django.apps import AppConfig
from django.db.models import CASCADE, ForeignKey


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Основное приложение'