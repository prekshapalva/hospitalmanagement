from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    query = models.TextField()
def _str_(self):
    return self.name+ ""+self.email
