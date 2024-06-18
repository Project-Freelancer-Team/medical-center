from django.urls import path
from .views import ServiceView, ServiceDetailView


app_name = "service_app"

urlpatterns = [
    path("", ServiceView.as_view(), name="service"),
    path("<str:slug>", ServiceDetailView.as_view(), name="service_detail"),
]

