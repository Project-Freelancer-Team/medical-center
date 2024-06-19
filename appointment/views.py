from django.shortcuts import render, redirect
from django.views import View


from service.models import Services, ServieCategory
from users.models import DoctorsOrUsers
from .models import Appointment


# Decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class AppointmentView(View):
    template_name = "appointment.html"
    
    def  get_context_data(self):
        context = {
            "services" : ServieCategory.objects.all(),
            "doctors" : DoctorsOrUsers.objects.filter(is_doctor = True)
        }
        return context
    
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context_data()
        name_and_surname = request.POST.get("name_surname")
        service = ServieCategory.objects.get(id = request.POST.get("service"))
        doctor = DoctorsOrUsers.objects.get(id = request.POST.get("doctor"), is_doctor=True)
        user = DoctorsOrUsers.objects.get(id=request.user.id)
        date = request.POST.get("date")
        time = request.POST.get("time")
        if "appointment" in request.POST:
            object = Appointment.objects.create(
                name_and_surname = name_and_surname,
                service = service,
                doctor = doctor,
                date = date,
                time = time,
                user = user
            )
            return redirect("main_app:home")
        return render(request, self.template_name, context)
    