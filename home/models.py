from django.db import models
# Create your models here.
#here m
class Patient(models.Model):
    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    age = models.TextField()
    gender = models.TextField()
    contact = models.TextField()
    email = models.EmailField()
    address = models.TextField()
def _str_(self):
    return self.name+ ""+self.gender
