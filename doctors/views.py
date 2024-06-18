from django.shortcuts import render
from django.views import View

from users.models import DoctorsOrUsers
from service.models import ServieCategory

class DoctorsView(View):
    template_name = "pages/specialists/doctor-2.html"
    
    
    def get_context_data(self, full_name=None, category=None):
        doctors = DoctorsOrUsers.objects.filter(is_doctor=True)
        if full_name:
            doctors = doctors.filter(first_name__icontains=full_name) | doctors.filter(last_name__icontains=full_name)
        if category:
            doctors = doctors.filter(servicedoctor__service_id=category).distinct()

        context = {
            "doctors": doctors,
            "service": ServieCategory.objects.all()
        }
        return context
    
    def get(self, request):
        full_name = request.GET.get('full_name')
        category = request.GET.get('category')
        context = self.get_context_data(full_name, category)
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)


class DoctorsDetailView(View):
    template_name = "pages/specialists/doctor-details.html"
    
    
    def get_context_data(self, *args, **kwargs):
        context = {
            "doctor" : DoctorsOrUsers.objects.get(is_doctor=True, username = self.kwargs["username"])
        }
        return context
    
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)