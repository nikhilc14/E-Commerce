
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class auction_listings(models.Model):
    name = models.CharField(max_length=256)
    price = models.ForeignKey('bids', on_delete=models.CASCADE)
    description = models.TextField(default='')
    created_on = models.DateTimeField()
    url = models.URLField(blank=True)

class bids(models.Model):
    listing = models.ForeignKey(auction_listings, on_delete=models.CASCADE,default='')
    start_bid = models.FloatField(default=0.0)
    current_bid = models.FloatField(default=0.0)
    final_bid = models.FloatField(default=0.0)



