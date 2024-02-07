
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *




urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/',Myprofile,name='myprofile'),
    path('Register/', Registrationform.as_view(), name='Registrationform'),

]
