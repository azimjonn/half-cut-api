from django.db import models

class DataSample(models.Model):
    image_name = models.CharField(max_length=100)
    left = models.FloatField()
    right = models.FloatField()
