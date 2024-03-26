from django.urls import path
from core2.views import ProductionView,ContactView

urlpatterns = [
    path("products/",ProductionView.as_view(),name="product"),
    path("contact/",ContactView.as_view(),name="contact")
]
