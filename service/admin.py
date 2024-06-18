from django.contrib import admin
from .models import Services


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display = ["name"]
