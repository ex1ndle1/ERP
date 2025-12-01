from django.contrib import admin
from django.urls import path
from .views import home, course, contact_view

app_name  = 'erp'

urlpatterns = [
  path('home/' , home, name='home' ),
  path('course/student/<int:student_id>/', course, name='course_detail'),
  path('contact/', contact_view, name='contact')
 
]