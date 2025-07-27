from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    aadhaar = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    purpose = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name