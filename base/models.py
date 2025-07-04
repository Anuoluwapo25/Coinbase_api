from django.db import models


class Product(models.Model):
    Product_name = models.CharField(max_length=125)
    Description = models.CharField(max_length=255)
    image = models.ImageField(
    upload_to='products/', 
    blank=True,             
    null=True,              
    help_text="Upload product image"
)
    category = models.CharField(max_length=125)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    