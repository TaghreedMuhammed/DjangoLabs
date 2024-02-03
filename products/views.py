from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
product_list = [
    {'id': 1, 'Name': 'Converse', 'Image': 'convwomen.jpg', 'category':'Women','price':"700"},
    {'id': 2, 'Name': 'Converse', 'Image': 'convwomen2.jpg','category':'Women','price':"700"},
    {'id': 3, 'Name': 'Converse', 'Image': 'nikemen1.jpg','category':'Men','price':"700"},
    {'id': 4, 'Name': 'Men Shoes', 'Image': 'nikemen2.jpg','category':'Men','price':"700"},

]
def home(request):
    return HttpResponse('<h1 style="background-color:azure;text-align:center;margin-top:200px">Welcome To Our Store</h1>')

def products(request):
    database_product_list = Products.objects.all()
    context = {'product_list': product_list,
               'database_product_list': database_product_list}
    return render(request, 'products/parent.html', context)

def product_details(request, productId):
    product = next((p for p in product_list if p['id'] == productId), None)

    if product:
        # details=Products.objects.get(id=productId)
        context = {'product': product
               }
        return render(request, 'products/product_details.html', context)
    else:
        return HttpResponse('Product not found.')

# def actions(request):
#     context={'products':Products.objects.all()}
#     return render (request, 'products/parent.html', context)

def about(request):
   return render(request,'products/about.html')

def productsAdd(request):
    if(request.method=='POST'):
        Products.objects.create(name=request.POST['pname'],
                                price=request.POST['pprice'])
        request.POST['pname']
        request.POST['pprice']
        return HttpResponseRedirect('/Products/')

    return render(request,'products/add.html')

def productsDelete(request,productId):
     Products.objects.filter(id=productId).delete()

     return HttpResponseRedirect('/Products/')

