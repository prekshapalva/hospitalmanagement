from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url
from . import views
# Django admin customization
#check admin site prekshaa
admin.site.site_title = "Admin site"
admin.site.site_header = "Hopitalmanagement - Admin Dashboard"
admin.site.index_title = "Hopitalmanagement - Admin Dashboard"

urlpatterns = [
    path('', views.about, name='about'),
    path('administrator', views.administrator, name='administrator'),
    path('doctors', views.doctors, name='doctors'),
    path('patient_main', views.patient_main, name='patient_main'),
    path('add_doctor_by_admin', views.add_doctor_by_admin, name='add_doctor_by_admin'),
    path('patient', views.patient, name='patient'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login')
]