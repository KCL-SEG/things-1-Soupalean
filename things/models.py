from django.db import models


# Create your models here.


def inRange(integer):
    if 101 > integer >= 0:
        return integer
    raise AttributeError("quantity out of range")


class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(validators=[inRange])
