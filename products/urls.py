from django.contrib import admin
from django.urls import path,include
from products import views

# from lab.settings import *

urlpatterns = [
    path('new',views.productsAdd,name='productsAdd'),
    path('NewForm',views.productsAddForm,name='productsAddForm'),
    path('delete/<int:productId>',views.productsDelete,name='productsDelete'),
    path('update/<int:productId>',views.productsUpdate,name='productsUpdate'),
    path('', views.products, name='products'),
    path('details/<int:productId>/', views.product_details, name='product_details'),
             ]
