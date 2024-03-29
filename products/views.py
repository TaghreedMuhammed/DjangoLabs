from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
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
    context = {
               'database_product_list': database_product_list}
    return render(request, 'products/parent.html', context)

def product_details(request, productId):
        details=Products.objects.get(id=productId)
        context = {'details': details}
               
        return render(request, 'products/product_details.html', context)
 



def about(request):
   return render(request,'products/about.html')

@login_required
def productsAdd(request):
    if(request.method=='POST'):
        Products.objects.create(name=request.POST['pname'],
                                price=request.POST['pprice'],
                                image=request.FILES['pimage'],
                                )
        
        return HttpResponseRedirect('/Products/')
    
    
    # context={'Products':Products.objects.all()}
    return render(request,'products/add.html')

@login_required
def productsDelete(request,productId):
     Products.objects.filter(id=productId).delete()
     
     return HttpResponseRedirect('/Products/')

@login_required
def productsUpdate(request, productId):
    product = Products.objects.get(id=productId)
    context = {'product': product}

    if request.method == 'POST':
        pname = request.POST['pname']
        if 'pimage' in request.FILES:
            pimage = request.FILES['pimage']

        if 'pprice' in request.POST:
            pprice = request.POST['pprice']
            product.name = pname
            product.image = pimage
            product.price = pprice
            product.save()

        return HttpResponseRedirect('/Products/')
    else:
        context['text'] = "Please Fill all fields"

    return render(request, 'products/update.html', context)

    
@login_required
def productsAddForm(request):
    form = ProductForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                name=request.POST['name'],
                price=request.POST['price'],
                image=request.FILES['image'],
                category=Category.objects.get(id=request.POST['category'])
            )
            return HttpResponseRedirect('/Products/')
    else:
        context['textt'] = "Data Not Complete"

    return render(request, 'products/addForm.html', context)

