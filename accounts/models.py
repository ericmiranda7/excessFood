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

    def __str__(self):
        return self.user.username

class Address(models.Model):
    name = models.CharField(max_length=30)
    addr = models.TextField()
