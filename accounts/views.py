from django.shortcuts import render,redirect
from django.contrib.auth.forms import authenticate
from django.shortcuts import reverse
from products.models import Products
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def Mylogin(request):
    context={'form':authenticate()}
    return render(request,'registrations/login.html',context)

def Myprofile(request):
    context={'products':Products.objects.all()}
    return render(request,'products/parent.html',context)

class Registrationform(CreateView):
    model=User
    template_name='registration/register.html'
    form_class=UserCreationForm
    context_object_name='form'
    success_url=reverse_lazy('login')


    