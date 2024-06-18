from django.db import models
from users.models import DoctorsOrUsers



class Services(models.Model):
    image = models.ImageField(upload_to="service/", blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name
