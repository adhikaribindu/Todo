from django import forms 


class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=27)
    first_name=forms.CharField(max_length=27)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=320)
    password=forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()