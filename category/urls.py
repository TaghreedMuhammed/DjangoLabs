from django.contrib import admin
from django.urls import path,include
from category import views
from .views import CategoryUpdatee
from .views import CategoryUpdateegeneric
from .views import CategoryDetails
from .views import CategoryDelete
from .views import CategoryList
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('new',views.categoryAdd, name='categoryAdd'),
    path('new',login_required(views.CategoryAddGeneric.as_view()), name='categoryAdd'),
    path('Add/',views.categoryAddForm, name='categoryForm'),
    path('delete/<int:productId>',views.categoryDelete,name='categoryDelete'),
    #path('Update/<int:productId>',views.categoryUpdate,name='categoryUpdate'),
    # path('Update/<int:productId>',CategoryUpdatee.as_view(),name='categoryUpdatee'),
    path('Update/<pk>',login_required(CategoryUpdateegeneric.as_view()),name='categoryUpdatee'),
    path('', views.category, name='category'),
    path('<pk>',CategoryDetails.as_view(), name='categoryDetails'),
    path('Delete/<pk>',login_required(CategoryDelete.as_view()), name='categoryDelete'),
    path('List/<pk>',CategoryList.as_view(), name='categoryList'),
]