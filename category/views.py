from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.


product_list = [
    {'id': 1, 'Name': 'Converse', 'Image': 'convwomen.jpg', 'category':'Women','price':"700"},
    {'id': 2, 'Name': 'Converse', 'Image': 'convwomen2.jpg','category':'Women','price':"700"},
    {'id': 3, 'Name': 'Converse', 'Image': 'nikemen1.jpg','category':'Men','price':"700"},
    {'id': 4, 'Name': 'Men Shoes', 'Image': 'nikemen2.jpg','category':'Men','price':"700"},
    {'id': 5, 'Name': 'Men Shoes', 'Image': 'nikemen2.jpg','category':'Men','price':"700"},
    {'id': 6, 'Name': 'Men Shoes', 'Image': 'nikemen2.jpg','category':'Men','price':"700"},
    {'id': 7, 'Name': 'Men Shoes', 'Image': 'nikemen2.jpg','category':'Men','price':"700"},
]

def category(request):
    database_product_category = Category.objects.all()
    context = {'product_list': product_list,
                'database_product_category': database_product_category}
    return render(request, 'category/category.html', context)

def categoryAdd(request):
    if(request.method=='POST'):
        Category.objects.create(name=request.POST['pname'],
                                category=request.POST['pcat'])
        request.POST['pname']
        request.POST['pcat']
        return HttpResponseRedirect('/Category/')

    return render(request,'category/categoryadd.html')

def categoryDelete(request,productId):
     Category.objects.filter(id=productId).delete()

     return HttpResponseRedirect('/Category/')

def updateProducts(request,productId):
    Category.objects.filter(id=productId).update()
    return HttpResponseRedirect('/Category/')

