from django.db import models
from django.contrib.auth.models import User

class CustomerChargeData(models.Model):
    user               = models.ForeignKey(User)
    stripe_customer_id = models.CharField(max_length=255)
    card_type          = models.CharField(max_length=20)
    card_last4         = models.CharField(max_length=4)

class Product(models.Model):
    name               = models.CharField(max_length=80)
    description        = models.CharField(max_length=255)
    product_identifier = models.CharField(max_length=255)
    price              = models.DecimalField(max_digits=10, decimal_places=2)

    def price_in_cents(self):
        return int(self.price * 100)

class Purchase(models.Model):
    product   = models.ForeignKey(Product)
    user      = models.ForeignKey(User)
