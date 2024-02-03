from django.contrib import admin
from django.urls import path,include
from products import views

urlpatterns = [
    path('new',views.productsAdd,name='productsAdd'),
    path('delete/<int:productId>',views.productsDelete,name='productsDelete'),
    path('', views.products, name='products'),
    path('<int:productId>/', views.product_details, name='product_details'),
             ]