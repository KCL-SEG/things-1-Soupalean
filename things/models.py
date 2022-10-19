from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


def inRange(integer):
    if 101 > integer >= 0:
        return True
    return False


class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
