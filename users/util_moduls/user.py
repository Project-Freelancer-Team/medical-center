from django.shortcuts import  redirect
from django.contrib.auth.backends import BaseBackend
from users.models import DoctorsOrUsers
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.db import IntegrityError

def register(request):
    if request.method == 'POST' and "register" in request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

            # Check if passwords match
        if password != confirm_password:
            messages.error(request,"Пароли не совпадают!")
            return redirect("users:register")

        # Create the user
        try:
            user_check = DoctorsOrUsers.objects.get(email=email)
            if user_check:
                messages.error(request, 'Пользователь с таким адресом электронной почты уже существует.')
                return redirect("users:register")
            else:
                redirect("users:login")
        except Exception as e:
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
                messages.error(request, 'Пользователь с таким  именем пользователя уже существует.')
                return redirect("users:register")
            else:
                messages.error(request, 'Database error: Unable to register user')
                return redirect('users:register')
        except Exception as err:
            messages.error(request,err)
            return redirect("users:register")
        
    return redirect("users:login")


def login_user(request):
    if request.method == "POST" and  "login" in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main_app:home")
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect("users:login")
    else:
        pass


class EmailOrUsernameModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('username')
            
        try:
            user = DoctorsOrUsers.objects.get(username=username)
        except DoctorsOrUsers.DoesNotExist:
            try:
                user = DoctorsOrUsers.objects.get(email=username)
            except DoctorsOrUsers.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

    def get_user(self, user_id):
        try:
            return DoctorsOrUsers.objects.get(pk=user_id)
        except DoctorsOrUsers.DoesNotExist:
            return None