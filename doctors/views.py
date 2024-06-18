from django.shortcuts import render
from django.views import View

from users.models import DoctorsOrUsers

class DoctorsView(View):
    template_name = "pages/specialists/doctor-2.html"
    
    
    def get_context_data(self):
        context = {
            "doctors": DoctorsOrUsers.objects.filter(is_doctor=True)
        }
        return context
    
    
    def get(self, request):
        context = self.get_context_data()
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