from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from authentication.forms import RegistrationForm,LoginForm
from django.contrib.auth import  login,authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.

User=get_user_model()



def auth_login(request):
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data=form.cleaned_data
            user=authenticate(request,username=data.get("username"),password=data.get("password"))
            login(request, user)
            return redirect("/profile")
      
def login_view(request):
    form=LoginForm
    context={
        "form":form
    }
    return render(request,"login.html",context=context)
        

@login_required(login_url="/login_page")
def profile(request):
    return render(request,"profile.html")


def logout_view(request):
    # logout(request)
    pass

def register_view(request):
    form=RegistrationForm
    context={
        'form':form
    }
    return render(request,"register.html",context=context )


def save_user(request):
    if request.method=="POST":
        form=RegistrationForm(data=request.POST)
        form.is_valid()
        data=form.cleaned_data
        print(form.cleaned_data)

        try:

            user=User.objects.create(
             username=data.get("username"),
             first_name=data.get("first_name"),
             last_name=data.get("last_name"),
                email=data.get("email")
            )
            user.set_password(data.get("password"))
            user.save()
            messages.success(request,"User registered sucessfully")
        except IntegrityError:
            messages.error(request, "User with this username already exists")

        
        return redirect("/register_page")
    
