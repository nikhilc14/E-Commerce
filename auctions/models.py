from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction_listings(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField(default=0.0)
    created_on = models.DateTimeField()

class bids(models.Model):
    pass
