from django import forms
 


class TodoForm(forms.Form):
    title=forms.CharField(max_length=50)
    description=forms.CharField()

class LoginForm(forms.Form):
    user_name=forms.CharField()
    password=forms.CharField()