from django.db import models
from category.models import *

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=500)
    # category=models.CharField(max_length=100,default="women/men")
    createdate=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='products/images/',blank=True,null=True)
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    def get_image_url(self):
        return f'/media/{self.image}'
    
    def __str__(self):
        return self.name
    
    @classmethod
    def products(self):
        return self.objects.all()
    
    @classmethod
    def product_details(cls,productId):
        return cls.objects.get(id=productId)


