from accounts.models import Address, Donator
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.gis.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=32)
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE)
    food_type = (('v', 'Vegetarian'), ('nv', 'Non Vegetarian'))
    category = models.CharField(
        max_length=2,
        choices=food_type,
        help_text="Veg or Non Veg"
        )
    qty = models.IntegerField()
    added_at = models.DateTimeField()
    expiry = models.DateTimeField()
    address = ChainedForeignKey(
        Address,
        chained_field='donator',
        chained_model_field='donator',
        show_all=False,
        auto_choose=True,
        sort=True,
    )
    photo = models.ImageField()
    tags = (('T', 'Tentative'), ('E', 'Emergency'), ('S', 'Expiring soon'), ('N', 'None'))
    tag = models.CharField(
        max_length=2,
        choices=tags,
        default='N',
        )
    location = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.name