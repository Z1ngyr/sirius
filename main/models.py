from django.db import models


class QRCodeData(models.Model):
    data = models.TextField()
