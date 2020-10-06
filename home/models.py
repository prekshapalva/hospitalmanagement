from django.db import models

# Model for Patient (appointment)
class Patient(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField(default="", editable=False)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    doctor = models.CharField(max_length=30, null=True)
    desc = models.CharField(max_length=200, null=True)
    date = models.DateField(default="", editable=False)
    time = models.TimeField(default="", editable=False)
    status = models.CharField(max_length=500)
    details = models.TextField(max_length=1024 * 2, default="Date:\nReason for visit:\nPrescription:\nTests:\nSummary:\nNext visit:")

    def __str__(self):
        return str(self.name)
        #return self.name

# Model for Doctor (details)
class Doctor(models.Model):
    doc_name = models.CharField(max_length=30)
    doc_dob = models.CharField(max_length=30)
    doc_age = models.CharField(max_length=30)
    doc_gender = models.CharField(max_length=30)
    doc_contact = models.CharField(max_length=30)
    doc_email = models.EmailField()
    doc_address = models.CharField(max_length=100)
    doc_degree = models.CharField(max_length=300)
    doc_desc = models.CharField(max_length=200)

    def __str__(self):
        return str(self.doc_name)

    #def __str__(self):
        #return self.doc_name
