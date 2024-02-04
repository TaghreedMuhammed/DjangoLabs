from django import forms
from .models import *
from django.core.exceptions import ValidationError
from category.models import *

class ProductForm(forms.Form):
    name=forms.CharField(max_length=200,required=True)
    price=forms.IntegerField(required=True)
    image=forms.ImageField(required=True)
    category=forms.ChoiceField(choices=Category.get_category())
    
    

    def class_name(self):
        enteredName=self.cleaned_data['name']
        obj1= Products.objects.get(name=enteredName).exists()
        if(obj1):
            raise ValidationError('Name already exists')
        
        else:
            return True

