from django.db import models
from service.models import Services, ServieCategory
from users.models import DoctorsOrUsers


class Appointment(models.Model):
    for_consultation = models.BooleanField(default=False, blank=True, null=True)
    name_and_surname = models.CharField(max_length=250)
    service = models.ForeignKey(ServieCategory, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(DoctorsOrUsers, on_delete=models.CASCADE, related_name="appointments_doctor")
    user = models.ForeignKey(DoctorsOrUsers, on_delete=models.CASCADE, related_name="user_appointments")
    date = models.DateField()
    time = models.TimeField()
    
    date_created = models.DateTimeField(auto_now_add=True)
 
    
    def __str__(self) -> str:
        return self.name_and_surname
    

    
