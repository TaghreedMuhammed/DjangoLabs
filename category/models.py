from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=500)
    category=models.CharField(max_length=100,default="women/men")
   
