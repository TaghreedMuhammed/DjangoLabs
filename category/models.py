from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    # category=models.CharField(max_length=100,default="women/men")
    

    @classmethod
    def get_category(cls):
         return [(p.id,p.name)for p in cls.objects.all()]
       
       
      
    def str(self):
        return self.name  