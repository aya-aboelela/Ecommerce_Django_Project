from django.db import models
from unicodedata import name
from statistics import mode
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    desc = models.TextField(max_length=5000)
    image = models.ImageField()
    price = models.DecimalField(max_digits=11,decimal_places=2)
    category_id = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class order(models.Model):
    productid = models.IntegerField()
    user_id = models.IntegerField()
    num =models.IntegerField()