from django.contrib import admin
from home.models import Patient, Doctor
# Register your models here.
#changed from contacts
#admin.site.register(Patient)
class AdminPatient(admin.ModelAdmin):
    model = Patient
    list_display = ('date','time','doctor','name','age','gender','dob','contact','email','desc')
    list_filter = ("date","time","doctor")
admin.site.register(Patient, AdminPatient)

class AdminDoctor(admin.ModelAdmin):
    model = Doctor
    list_display = ('doc_name','doc_age','doc_gender','doc_dob','doc_contact','doc_email','doc_desc')
    list_filter = ("doc_name","doc_age")
admin.site.register(Doctor, AdminDoctor)
