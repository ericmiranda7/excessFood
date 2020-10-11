from django.db import models

# Create your models here.
""" Name: str
Type(veg /nv): char choice
Qty: int
Expiry: date
Address: str
User - foreign key
"""

class Food(models.Model):
    name = models.CharField(max_length=32)
    
    food_type = (('v', 'Vegetarian'), ('nv', 'Non Vegetarian'))
    category = models.CharField(
        max_length=2,
        choices=food_type,
        help_text="Veg or Non Veg"
        )
    qty = models.IntegerField()
    added_at = models.DateTimeField()
    expiry = models.DateTimeField()
    address = models.TextField()

    def __str__(self):
        return self.name