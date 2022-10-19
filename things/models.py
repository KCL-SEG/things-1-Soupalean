from django.db import models

# Create your models here.


class Thing(models.Model()):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()