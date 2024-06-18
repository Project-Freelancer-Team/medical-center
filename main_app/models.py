from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=250)
    person_job = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name