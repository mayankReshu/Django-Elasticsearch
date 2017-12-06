from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    age = models.IntegerField(null=False,blank=False)
    fname = models.CharField(max_length=250, null=False,blank=False)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    phone = models.IntegerField(null=False,blank=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    