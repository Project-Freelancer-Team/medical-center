from django.urls import path
from .views import HomeView, ReviewView, contact, consult

app_name  = "main_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("review/", ReviewView.as_view(), name="review"),
    path('contact/', contact, name='contact'),
    path('consultation/', consult, name='consult')
]
