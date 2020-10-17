from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.
class Donator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    addresses = models.ManyToManyField('Address')
    location = models.PointField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Address(models.Model):
    name = models.CharField(max_length=30)
    addr = models.TextField()

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    profession = models.CharField(max_length=32)
    skill_set = models.CharField(max_length=32)
    # subscribe  = models.BooleanField()
    # terms_condition = models.BooleanField()
    # addresses = models.ManyToManyField('Address')

    def __str__(self):
        return self.user.username

