from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'erp/index.html' )

@login_required
def course(request):
    return  render(request, 'erp/course.html')


 