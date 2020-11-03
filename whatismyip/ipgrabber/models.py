from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length = 100)
    ip = models.GenericIPAddressField())
    bodytext = models.TextField()
    timestamp = models.DateTimeField()