from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    age = models.IntegerField(null=False,blank=False)
    