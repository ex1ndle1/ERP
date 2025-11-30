from django import forms 
from .models import Teacher,Student
from django.contrib.auth.models import User

class RegisterTeacherForm(forms.Form):
    
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,label='enter ur password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='confirm password')
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    specialization  = forms.CharField(required=True)
    experience = forms.IntegerField(required=True)
    
        

    def clean(self):
        try:
         cleaned_data = super().clean()
         if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError('diffrent passwords')
        except Exception:
           raise forms.ValidationError('Phone or email already registered in site')
        return cleaned_data
    

    def save(self):
        user = User.objects.create_user(
        email=self.cleaned_data['email'],
        username= self.cleaned_data['username'],
        password=self.cleaned_data['password1']

        )
        try:
         teacher = Teacher.objects.create(
            user=user,
            name = self.cleaned_data['name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            phone = self.cleaned_data['phone'],
            specialization = self.cleaned_data['specialization'],
            experience = self.cleaned_data['experience']
        
        )
        except Exception:
           user.delete()
           raise 
     
        return teacher
    

class RegisterStudentForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,label='enter ur password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='confirm password')
    name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)


    def clean(self):
        try:
         cleaned_data = super().clean()
         if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError('diffrent passwords')
        except Exception:
           raise forms.ValidationError('Phone or email already registered in site')
        return cleaned_data
    
    def save(self):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
        username= self.cleaned_data['username'],
        password=self.cleaned_data['password1']

        )
        try:
         student = Student.objects.create(
            user=user,
            name = self.cleaned_data['name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            phone = self.cleaned_data['phone'],
           
        
        )
        except Exception:
           user.delete()
           raise 
     
        return student
    



class LoginByEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginByPhoneForm(forms.Form):
   phone = forms.IntegerField()
   password = forms.CharField(widget=forms.PasswordInput)
    
# user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField()
#     last_name =  models.CharField()
#     phone = models.IntegerField(max_length=18)
#     specialization = models.CharField()
#     experience = models.IntegerField()




