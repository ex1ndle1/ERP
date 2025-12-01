
from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="your name")
    email = forms.EmailField(label="your email")
    message = forms.CharField(widget=forms.Textarea, label="message")