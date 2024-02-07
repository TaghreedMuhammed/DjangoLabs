from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=100)

   
    

    @classmethod
    def get_category(cls):
         return [(p.id,p.name)for p in cls.objects.all()]
    
    @classmethod
    def Getall(cls):
        return cls.objects.all()
    
    @classmethod
    def updateCategory(cls,productId):
        return cls.objects.get(id=productId)
       
       
      
    def str(self):
        return self.name  