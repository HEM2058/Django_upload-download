from django.db import models

# Create your models here.
class UploadFil(models.Model):
    file = models.FileField(null=True)

