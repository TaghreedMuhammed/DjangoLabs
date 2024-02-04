from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.




def category(request):
    database_product_category = Category.objects.all()
    context = {
                'database_product_category': database_product_category}
    return render(request, 'category/category.html', context)

def categoryAdd(request):
    if(request.method=='POST'):
        Category.objects.create(name=request.POST['pcat'],
                                )
       
        return HttpResponseRedirect('/Category/')

    return render(request,'category/categoryadd.html')

def categoryDelete(request,productId):
     Category.objects.filter(id=productId).delete()

     return HttpResponseRedirect('/Category/')

# def updateProducts(request,productId):
#     Category.objects.filter(id=productId).update()
#     return HttpResponseRedirect('/Category/')

