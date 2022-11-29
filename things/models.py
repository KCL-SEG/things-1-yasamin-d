from django.db import models

# Create your models here.
class Things(models.Model):
    name = models.CharField()(max_length=30, blank=False, unique=True)
    description = models.CharField()(max_length=120, blank=True)
    quantity = models.IntegerField()(MinValueValidator=0, MaxValueValidator=100)
