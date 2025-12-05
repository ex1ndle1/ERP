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

            user = None
            role = None
            role_id = None
            try:
                teacher = Teacher.objects.get(email=email)
                user = teacher.user
                role = 'teacher'
                role_id = teacher.id
            except Teacher.DoesNotExist:
                pass
            if user is None:
                try:
                    student = Student.objects.get(email=email)
                    user = student.user
                    role = 'student'
                    role_id = student.id
                except Student.DoesNotExist:
                    return render(request, "user/login_by_email.html", {"form": form, "error": "Email not registered"})
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user:
                login(request, auth_user)

                if role == 'student':
                    student = Student.objects.get(user=auth_user)
                    course = student.course  
                    return render(request, "erp/course.html", {"course": course})
                return redirect(f"/course/{role}/{role_id}")

            return render(request, "user/login_by_email.html", {"form": form, "error": "Incorrect password"})

    form = LoginByEmailForm()
    return render(request, "user/login_by_email.html", {"form": form})

# "/course/{role}/{role_id}
def login_by_phone(request):
    if request.method == "POST":
        form = LoginByPhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            user = None
            role = None
            role_id = None

            try:
                teacher = Teacher.objects.get(phone=phone)
                user = teacher.user
                role = 'teacher'
                role_id = teacher.id
            except Teacher.DoesNotExist:
                pass

            if not user:
                try:
                    student = Student.objects.get(phone=phone)
                    user = student.user
                    role = 'student'
                    role_id = student.id
                except Student.DoesNotExist:
                    return render(request, "user/login_by_phone.html", {"form": form,"error": "Phone number is not registered"})

            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                return redirect(f"/course/{role}/{role_id}")

            return render(request, "user/login_by_phone.html", {"form": form,"error": "Incorrect password"})

    form = LoginByPhoneForm()
    return render(request, "user/login_by_phone.html", {"form": form})




