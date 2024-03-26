from django.urls import path
from .views import TestAPIView,UserAPIView

urlpatterns = [
    path("test/",TestAPIView.as_view(),name="test-api-view"),
    path("user/",UserAPIView.as_view(),name="user-api-view")
]
