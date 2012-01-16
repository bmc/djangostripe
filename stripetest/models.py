from django.db import models

class Customer(models.Model):
    last_name          = models.CharField(max_length=30)
    first_name         = models.CharField(max_length=30)
    middle_initial     = models.CharField(max_length=1)
    address1           = models.CharField(max_length=55)
    address2           = models.CharField(max_length=55)
    city               = models.CharField(max_length=25)
    state              = models.CharField(max_length=2)
    postal_code        = models.CharField(max_length=10)
    stripe_customer_id = models.CharField(max_length=255)

class Product(models.Model):
    name               = models.CharField(max_length=80)
    description        = models.CharField(max_length=255)
    product_identifier = models.CharField(max_length=255)
    price              = models.DecimalField(max_digits=10, decimal_places=2)

class Purchase(models.Model):
    product   = models.ForeignKey(Product)
    customer  = models.ForeignKey(Customer)
    auth_code = models.CharField(max_length=255)
    pending   = models.BooleanField(default=True)