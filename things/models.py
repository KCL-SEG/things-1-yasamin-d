from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Things(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
