from django.urls import path
from .views import BlogMainView, BlogDetailView

app_name = "blog"

urlpatterns = [
    path("", BlogMainView.as_view(), name="blog_main"),
    path("detail/<str:slug>", BlogDetailView.as_view(), name="blog_detail"),
    path("detail/<str:slug>", BlogDetailView.as_view(), name="blog_detail"),
]
