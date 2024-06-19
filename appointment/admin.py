from django.contrib import admin
from .models import Appointment
from datetime import date, timedelta


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name_and_surname', 'service', 'doctor', 'user', 'date', 'time')
    list_filter = ('doctor', 'service', 'for_consultation', 'date')

    # Custom date filters
    def get_tomorrow(self, request, queryset):
        tomorrow = date.today() + timedelta(days=1)
        return queryset.filter(date=tomorrow)

    def get_day_after_tomorrow(self, request, queryset):
        day_after_tomorrow = date.today() + timedelta(days=2)
        return queryset.filter(date=day_after_tomorrow)

    def get_next_week(self, request, queryset):
        next_week_start = date.today() + timedelta(days=1)
        next_week_end = next_week_start + timedelta(days=6)
        return queryset.filter(date__range=[next_week_start, next_week_end])

    # Specify which functions are available as filters
    get_tomorrow.short_description = 'Tomorrow'
    get_day_after_tomorrow.short_description = 'Day After Tomorrow'
    get_next_week.short_description = 'Next Week'

    # Override get_list_filter method to include custom filters
    def get_list_filter(self, request):
        # Add custom filters to existing list_filter
        custom_list_filter = super().get_list_filter(request)
        custom_list_filter += (('date', admin.DateFieldListFilter),)  # Add 'date' filter

        return custom_list_filter

admin.site.register(Appointment, AppointmentAdmin)