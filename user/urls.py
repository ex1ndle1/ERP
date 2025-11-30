from django.contrib import admin
from django.urls import path
from .views import teacher_register, login_choice,student_register,login_by_email,login_by_phone

app_name  = 'user'

urlpatterns = [
    path('teacher_register/', teacher_register, name='teacher_register'),
   
    path('student_register/', student_register, name='student_register' ),
    path('login_choice/', login_choice, name='login_choice'),
    path('login_by_email/', login_by_email, name='login_by_email'),
    path('login_by_phone', login_by_phone, name='login_by_phone')
    

]