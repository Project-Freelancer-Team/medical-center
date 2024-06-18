from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["name_and_surname", "service", "date", "time", "for_consultation"]
    list_filter  = ["service", "date", "time", "for_consultation"]
