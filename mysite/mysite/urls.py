
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

 
urlpatterns = [
    path('yelloo/', include('C:\Users\Ahmad\Desktop\courses\profile-rest-api\mysite\yelloo\urls.py')),
    path('admin/', admin.site.urls),
]
