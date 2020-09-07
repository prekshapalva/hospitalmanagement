from django.db import models


# Create your models here.
# here m
class Patient(models.Model):
    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    doctor = models.CharField(max_length=30, null=True)
    desc = models.CharField(max_length=200, null=True)
    date = models.DateField(default="", editable=False)
    time = models.TimeField(default="", editable=False)

    def __str__(self):
       return self.name
# return f"Date:{self.date} | Time:{self.time} | Doctor:{self.doctor} | Patient:{self.name} | " \
               #f"Contact:{self.contact}"
class Doctor(models.Model):
    namedoc = models.CharField(max_length=30)