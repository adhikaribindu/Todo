from django.urls import path
from attendance.views import student,home,contact


urlpatterns=[
    path('student_page',student),
    path('home',home,name="home"),
    path('contact',contact,name="contact")
]