from django.urls import path
from .views import DoctorsView, DoctorsDetailView

app_name = "doctors_app"

urlpatterns = [
    path("", DoctorsView.as_view(), name="doctors_home"),
    path("detail/<str:username>", DoctorsDetailView.as_view(), name="doctors_detail")
]
