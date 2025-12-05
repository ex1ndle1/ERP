from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Course
from user.models import Student, Teacher
from .forms import ContactForm
from django.conf import settings


# Create your views here.
def home(request):
    course = Course.objects.all()
    return render(request , 'erp/index.html' , {'courses':course})


@login_required(login_url='/login/')  
def course(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.user != student.user:
        return redirect('user:login_choice')

    courses = Course.objects.filter(student_course=student)

    return render(request, 'erp/course.html', {'student': student, 'courses': courses})




@login_required(login_url='/login/')
def course_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.user != teacher.user:
        return redirect('user:login_choice')

    courses = Course.objects.filter(teacher=teacher.name) 
    return render(request, 'erp/course_teacher.html', {'teacher': teacher, 'courses': courses})




def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                subject=f'message from {name}',
              
                message=message,
                from_email=settings.EMAIL_HOST_USER,  
                recipient_list= ['muzaffarilxomjonov@gmail.com'],
                
                fail_silently=False,

                
            )
            

            
            return render(request, 'erp/index.html')  
    else:
        form = ContactForm()
    return render(request, 'erp/contact.html', {'form': form})
 