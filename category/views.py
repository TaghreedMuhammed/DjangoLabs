from django.shortcuts import render,reverse
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views import View
from django.views.generic import UpdateView,DetailView,DeleteView,ListView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.




def category(request):
    database_product_category = Category.objects.all()
    context = {'category': Category.Getall(),
                'database_product_category': database_product_category}
    return render(request, 'category/category.html', context)

@login_required
def categoryAdd(request):
    if(request.method=='POST'):
        Category.objects.create(name=request.POST['pcat'])
         
                                
       
        return HttpResponseRedirect('/Category/')

    return render(request,'category/categoryadd.html')

@login_required
def categoryDelete(request,productId):
     Category.objects.filter(id=productId).delete()

     return HttpResponseRedirect('/Category/')

@login_required
def categoryAddForm(request):
    form = CategoryForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category'))

    return render(request, 'category/addcat.html', context)

class CategoryDetails(DetailView):
    model=Category
    template_name='category/details.html'
    context_object_name='category'
    

class CategoryDelete(DeleteView):
    model=Category
    template_name='category/delete.html'
    success_url=reverse_lazy('category')


class CategoryList(ListView):
    model=Category
    template_name='category/category.html' 
    context_object_name='database_product_category'

class CategoryAddGeneric(CreateView):
    model=Category
    template_name='category/addcat.html'
    form_class=CategoryForm
    success_url=reverse_lazy('category')

class CategoryUpdateegeneric(UpdateView):
    model= Category
    template_name='category/updateCategory.html'
    # context_object_name='form'
    form_class=CategoryForm
    success_url=reverse_lazy('category')



class CategoryUpdatee(View):
    def get(self, request, productId):
        print('get category update')
        context = {'form': CategoryForm(instance=Category.updateCategory(productId))}
        return render(request, 'category/updateCategory.html', context)

    def post(self, request, productId):
        print('post category update')
        form = CategoryForm(request.POST, instance=Category.updateCategory(productId))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category'))

category_update_view = CategoryUpdatee.as_view()


@login_required   
def categoryUpdate(request,productId):
    context={'form':CategoryForm(instance=Category.updateCategory(productId))}
    if(request.method=='POST'):
        form=CategoryForm(request.POST,instance=Category.updateCategory(productId))
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('category'))

    return render(request,'category/updateCategory.html', context)



    



  
    

    
        
       




