from django.shortcuts import render, redirect

from django.views import View

from .util_moduls import user
from .models import DoctorsOrUsers
from appointment.models import Appointment

# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
class RegisterView(View):
    template_name = "pages/auth/register.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        
        #Post Actions
        response = user.register(request)
        return response if response else render(request, self.template_name)


class LogInView(View):
    template_name = "pages/auth/login.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        #Post Actions
        response = user.login_user(request)
        
        return response if response else render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = "profile.html"
    
    def get_context_data(self):
        appointments = None
        user = DoctorsOrUsers.objects.get(id= self.request.user.id )
        if user.is_doctor == True:
            appointments = Appointment.objects.filter(doctor__id = user.id )
        else:
            appointments = Appointment.objects.filter(user__id = user.id )
            
        context = {
            "user" : user,
            "appointments" : appointments
        }    
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name,context)
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template_name,context)
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('/')