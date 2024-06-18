from django.urls import path
from .views import ServiceView, ServiceDetailView, service_category_deteaile


app_name = "service_app"

urlpatterns = [
    path("", ServiceView.as_view(), name="service"),
    path("<str:slug>", ServiceDetailView.as_view(), name="service_detail"),
    path('lechenie/<str:slug>/', service_category_deteaile, name='service_category_deteaile')
]

