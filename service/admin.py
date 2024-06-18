from django.contrib import admin
from .models import Services, ServieCategory, ServiceDoctor, SerivePrice


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display = ["name"]


admin.site.register(ServieCategory)
admin.site.register(ServiceDoctor)
admin.site.register(SerivePrice)