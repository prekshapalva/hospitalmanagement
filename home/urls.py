from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf.urls import url
# Django admin customization
#check admin site prekshaa
admin.site.site_title = "Admin site"
admin.site.site_header = "Welcome Preksha :)"
admin.site.index_title = "This is the Admin site"
urlpatterns = [
    path('', views.about, name='about'),
    path('administrator', views.administrator, name='administrator'),
    path('doctors', views.doctors, name='doctors'),
    path('patient', views.patient, name='patient'),
]