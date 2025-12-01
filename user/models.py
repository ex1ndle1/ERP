from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Teacher(models.Model):
    email = models.EmailField(unique=True, max_length=30, default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=20)
    phone = models.IntegerField( unique=True)
    specialization = models.CharField(max_length=20)
    experience = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.last_name}"



class Student(models.Model):
    email = models.EmailField(unique=True, max_length=30, default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=20)
    phone = models.IntegerField()
    payment_status = models.BooleanField(default=False)
    course = models.ForeignKey('erp.Course' , on_delete=models.CASCADE, related_name='student_course', default=1)
    def __str__(self):
        return f"{self.name} {self.last_name}"






