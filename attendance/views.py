from django.shortcuts import render
from django.http import HttpResponse
from attendance.models import Attendance

# Create your views here.
def student(request):
    record=Attendance.objects.all()
    context={
        "call":record,
        "user_name":"Bindu"
    }
    return render(request,"attendance.html",context=context)


def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
