from django.db import models
from django.contrib.auth.models import AbstractUser





class DoctorsOrUsers(AbstractUser):
    doctor_image = models.ImageField(upload_to="doctors/", blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    about_doctor = models.TextField(null=True, blank=True)
    doctor_type = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.username


class Specialities(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(DoctorsOrUsers, related_name="specialities", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Qualifications(models.Model):
    title = models.CharField(max_length=150)
    university_and_years = models.CharField(max_length=250)
    owner = models.ForeignKey(DoctorsOrUsers, related_name="qualifications", on_delete=models.CASCADE, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(DoctorsOrUsers, related_name="skills", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
