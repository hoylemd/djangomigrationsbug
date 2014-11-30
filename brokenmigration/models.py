from django.db import models

# Create your models here.

class Thing(models.Model);
    name = models.CharField(max_length=200)

class ThingList
    name = models.CharField(max_length=200)
    things = models.ManyToManyField('Thing')
