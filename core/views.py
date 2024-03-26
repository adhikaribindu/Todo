from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from core.models import Todo
from core.models import Profile
from core.form import TodoForm,LoginForm
from django.contrib import messages
# from django.contrib import login


# Create your views here.

def home_page(request):
    queryset=Profile.objects.all().first()
    print(timezone.now())

    context={
        "user_name":"Shristi",
        "call":queryset,
        "location":"Pokhara",
        "contact":983365
    }
    return render(request,"page.html",context=context)


def save_todo(request):
    if request.method=="POST":
        form=TodoForm(data=request.POST)
        form.is_valid()
        data=form.cleaned_data

        Todo.objects.create(
            title=data.get("title"),
            description=data.get("description"),
            user_name_id=1,
            date_time=timezone.now()
        )
        messages.success(request,"Information added")
        return redirect ("add_todo")



def add_todo(request):
    form=TodoForm
    context={
        "form":form
    }
    return render(request,"todo.html",context=context)



    # context={
    #     "user_name":"sita",
    #     "address":"Canada",
    #     "greeting":"Welcome"
    # }
#     queryset=Todo.objects.all()
#     context={
#         "user_name":"Bindu",
#         "address":"Canada",
#         "greeting":"Welcome",
#         "queryset":queryset
#         }
#     return  render(request,"index.html",context=context)

# def information():
#     context=[{
#         "name":"Shristi",
#         "age":24,
#         "location":"kathmanu"
#     },
#     {
    #   "name":"Ram",
    #   "age":20,
    #   "location":"pokhara" 
    # }]
    # # context={"name":"Sita","age":25}
    # return context


def details(request):
    # print(request.GET)
    todo=request.GET.get("todo")
    if todo=="past":
        # queryset=Todo.objects.all()
        queryset=Todo.objects.filter(date_time__lte=timezone.now())
    else :
        queryset=Todo.objects.filter(date_time__gte=timezone.now())
    context={
        "student_id":1,
        "todos":queryset,
        
        "name":"rajesh"
    }
    return render(request,"todos.html",context=context)

def about_page(request):
    context={
        "greeting":"welcome",
        "company_name":"Money_mitra",
        # "data": information()
    }
    return render(request,"todos.html",context=context)



def account(request):
    return HttpResponse("Welcome")

def register(request):
    return HttpResponse("Register Page")

def login(request):
    return HttpResponse("Open login page")

def system(request):
    return HttpResponse("The system is running")

def hardware(request):
    return HttpResponse("Brought some electric hardware")


