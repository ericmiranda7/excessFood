from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    addresses = models.ManyToManyField('Address')
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    points = models.IntegerField(default = 0)


    def __str__(self):
        return self.user.username

class Address(models.Model):
    name = models.CharField(max_length=30)
    addr = models.TextField()

    def __str__(self):
        return self.name
