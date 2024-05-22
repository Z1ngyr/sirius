from django.urls import path, include
from .views import generate_qr_code

urlpatterns = [
    path('generate-qr-code/', generate_qr_code, name='generate_qr_code'),
]
