from django.db import models
from users.models import DoctorsOrUsers



class Services(models.Model):
    image = models.ImageField(upload_to="service/", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name


class ServieCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_cate')
    image = models.ImageField(upload_to="service/", blank=True, null=True)

    def __str__(self):
        return self.name

class ServiceDoctor(models.Model):
    service = models.ForeignKey(ServieCategory, on_delete=models.CASCADE, related_name='service_doctor')
    doctor = models.ForeignKey(DoctorsOrUsers, on_delete=models.CASCADE)


class SerivePrice(models.Model):
    service = models.ForeignKey(ServieCategory, on_delete=models.CASCADE, related_name='service_price')
    name = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name
