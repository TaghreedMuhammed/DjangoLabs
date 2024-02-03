from django.contrib import admin
from django.urls import path,include
from category import views

urlpatterns = [
    path('new',views.categoryAdd, name='categoryAdd'),
    path('delete/<int:productId>',views.categoryDelete,name='categoryDelete'),
    path('', views.category, name='category'),
]