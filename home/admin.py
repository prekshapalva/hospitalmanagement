from django.contrib import admin
from home.models import Patient
# Register your models here.
#changed from contacts
#admin.site.register(Patient)
class AdminPatient(admin.ModelAdmin):
    model = Patient
    list_display = ('date','time','doctor','name','age','gender','dob','contact','email','desc')
    list_filter = ("date","time","doctor")
admin.site.register(Patient, AdminPatient)

