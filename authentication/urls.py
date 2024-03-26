from django.urls import path
from authentication.views import login_view,register_view,save_user,auth_login,profile


urlpatterns=[
    path('login_page',login_view,name="login"),
    path('register_page',register_view,name="register"),
    path("save-user/",save_user,name="save-user"),
    path("auth_login",auth_login,name="auth_login"),
    path("profile",profile,name="profile")
]