from django.db import models

# Create your models here.

class  Games(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()
