from django.contrib import admin
from home.models import Patient, Doctor
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Patient table
class AdminPatient(admin.ModelAdmin):
    model = Patient
    list_display = ('name','date','time','doctor','age','gender','dob','contact','email','desc')
    list_filter = ("doctor","date","time")
admin.site.register(Patient, AdminPatient)

# Doctor table
class AdminDoctor(admin.ModelAdmin):
    model = Doctor
    list_display = ('doc_name','doc_age','doc_degree','doc_gender','doc_dob','doc_contact','doc_email','doc_desc')
    list_filter = ("doc_name","doc_degree")
admin.site.register(Doctor, AdminDoctor)

