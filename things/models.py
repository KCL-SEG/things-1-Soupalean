from django.db import models

# Create your models here.


class Thing(models.model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
