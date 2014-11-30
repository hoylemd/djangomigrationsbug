from django.db import models

# Create your models here.


class ThingList(models.Model):
    name = models.CharField(max_length=200)
    things = models.CharField(max_length=200)
