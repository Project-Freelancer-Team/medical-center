from django.contrib import admin
from .models import DoctorsOrUsers, Qualifications, Skills, Specialities
from service.models import Services


class QualificationsInline(admin.TabularInline):
    model = Qualifications
    extra = 1  
    
    
class SpecialitiesInline(admin.TabularInline):
    model = Specialities
    extra = 1  
    
    
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1  
    
class DocotorsOrUserAdmin(admin.ModelAdmin):
    list_display = ["is_doctor", "username","first_name", "last_name"]
    list_filter = ["is_doctor"]
    inlines = [SpecialitiesInline,QualificationsInline, SkillsInline]
    
    
    def save_model(self, request, obj, form, change):

        if 'password' in form.cleaned_data:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)
   
admin.site.register(DoctorsOrUsers, DocotorsOrUserAdmin)
