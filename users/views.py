from django.shortcuts import render, redirect

from django.views import View

from .util_moduls import user
from .models import DoctorsOrUsers
from appointment.models import Appointment
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import *
# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.db import IntegrityError



class RegisterView(View):
    template_name = "pages/auth/register.html"

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']

            if password != confirm_password:
                messages.error(request, "Пароли не совпадают!")
                return redirect("users:register")

            try:
                user_check = DoctorsOrUsers.objects.get(email=email)
                if user_check:
                    messages.error(request, 'Пользователь с таким адресом электронной почты уже существует.')
                    return redirect("users:register")
            except DoctorsOrUsers.DoesNotExist:
                pass

            try:
                user = DoctorsOrUsers.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                return redirect("users:login")
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e):
                    messages.error(request, 'Пользователь с таким именем пользователя уже существует.')
                    return redirect("users:register")
                else:
                    messages.error(request, 'Database error: Unable to register user')
                    return redirect('users:register')
            except Exception as err:
                messages.error(request, str(err))
                return redirect("users:register")

        return render(request, self.template_name, {'form': form})


class LogInView(View):
    template_name = "pages/auth/login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main_app:home")
            else:
                messages.error(request, "Username or password is incorrect")
                return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


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