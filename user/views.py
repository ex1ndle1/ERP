from django.shortcuts import render, redirect
from .forms import RegisterTeacherForm,RegisterStudentForm,LoginByEmailForm,LoginByPhoneForm
from django.contrib.auth import authenticate,login
from .models import Teacher,Student
from django.contrib.auth.models import User
from erp.models import Course

# Create your views here.



def login_choice(request):
    return render(request, 'user/login_choice.html')

def teacher_register(request):

    if request.method == 'POST':
        form = RegisterTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login_choice')
        

    else:
        form = RegisterTeacherForm()

    return render(request, 'user/teacher_register.html', {'form':form})



def student_register(request):
    course = Course.objects.all()
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            
            student = form.save()
            if student.course:
                student.course.studiying_now += 1
                student.course.save()



            return redirect('user:login_choice')

    else:
        form = RegisterStudentForm()

    return render(request, 'user/student_register.html', {'form':form, 'courses':course})


def login_by_email(request):
    if request.method == "POST":
        form = LoginByEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return render(request, "user/login_by_email.html", {"form": form,"error": "Email not registered" })

            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                return redirect("erp:home")

            return render(request, "user/login_by_email.html", {"form": form,"error": "Incorrect password"})

    form = LoginByEmailForm()
    return render(request, "user/login_by_email.html", {"form": form})



def login_by_phone(request):
    if request.method == "POST":
        form = LoginByPhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            user = None
            try:
                teacher = Teacher.objects.get(phone=phone)
                user = teacher.user
            except Teacher.DoesNotExist:
                pass

            if not user:
                try:
                    student = Student.objects.get(phone=phone)
                    user = student.user
                except Student.DoesNotExist:
                    return render(request, "user/login_by_phone.html", {"form": form,"error": "Phone number is not registered"})

            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                return redirect("erp:home")

            return render(request, "user/login_by_phone.html", {"form": form,"error": "Incorrect password"})

    form = LoginByPhoneForm()
    return render(request, "user/login_by_phone.html", {"form": form})




