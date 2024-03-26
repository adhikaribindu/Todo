from django.urls import path
from core.views import account
from core.views import register
from core.views import login
from core.views import system
from core.views import hardware
from core.views import home_page
from core.views import about_page
# from core.views import information
from core.views import details
from core.views import add_todo,save_todo

urlpatterns=[
    path("",account),
    path("register",register),
    path("login",login),
    path("system",system),
    path("hardware",hardware),
    path("home_page",home_page),
    path("about_page",about_page),
    path("details",details),
    path("add_page",add_todo, name="add_todo"),
    path("save_page",save_todo, name="save_todo")
    # path("information",information)
]