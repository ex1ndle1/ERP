from django.contrib import admin
from django.urls import path
from .views import home, course

app_name  = 'erp'

urlpatterns = [
  path('home/' , home, name='home' ),
  path('course/', course, name='course'),

]