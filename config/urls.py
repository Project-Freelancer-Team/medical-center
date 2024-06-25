from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main_app.urls", namespace="main_app")),
    path('users/', include("users.urls", namespace="users")),
    path('service/', include("service.urls", namespace="service_app")),
    path('doctors/', include("doctors.urls", namespace="doctors_app")),
    path('blog/', include("blog.urls", namespace="blog")),
    path('appointment/', include("appointment.urls", namespace="appointment")),
     path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
