from django.db import models
from vendors.models import Vendor

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name