from home.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

# About, Admin, Doctor and Patient page view
def about(request):
    return render(request, 'about.html')
def administrator(request):
    return render(request, 'administrator.html')
def doctors(request):
    return render(request, 'doctors.html')
def patient_main(request):
    return render(request, 'patient_main.html')

# Patient list (all appointments)
def patient(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        doctor = request.POST['doctor']
        desc = request.POST['desc']
        date = request.POST['date']
        time = request.POST['time']
        # print(name,dob,age,gender)
        ins = Patient(name=name, dob=dob, age=age, gender=gender, email=email, contact=contact, address=address,
                      desc=desc, doctor=doctor, date=date, time=time)
        ins.save()
        print("The data is submitted to the database")
        # return HttpResponse("Contact Page(/contact)")
    return render(request, 'patient.html')
# Doctor details
def add_doctor_by_admin(request):
    if request.method == "POST":
        doc_name = request.POST['doc_name']
        doc_dob = request.POST['doc_dob']
        doc_age = request.POST['doc_age']
        doc_gender = request.POST['doc_gender']
        doc_email = request.POST['doc_email']
        doc_contact = request.POST['doc_contact']
        doc_address = request.POST['doc_address']
        doc_degree = request.POST['doc_degree']
        doc_desc = request.POST['doc_desc']
        # print(name,dob,age,gender)
        ins = Doctor(doc_name=doc_name, doc_degree=doc_degree, doc_dob=doc_dob,
                     doc_age=doc_age, doc_gender=doc_gender, doc_email=doc_email,
                     doc_contact=doc_contact, doc_address=doc_address, doc_desc=doc_desc)
        ins.save()
        print("The data is submitted to the database")
        # return HttpResponse("Contact Page(/contact)")
    return render(request, 'add_doctor_by_admin.html')

# Register form for the new doctor (by admin)
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            send_mail('Patient login details',
                      'Your appointment request is accepted \n\nLogin credentials:\nUsername - '
                      +user+ '\nPassword - '+password+ '\n\n\nThank you',
                      settings.EMAIL_HOST_USER,
                      [form.cleaned_data.get('email')],
                      fail_silently=False)
            messages.success(request, 'Account was created for '+ user )

            return redirect('login')
    context={'form': form}
    return render(request, 'register.html', context)

# Login for the new doctor after getting registered by admin
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin/home/patient/')
        else:
            messages.info(request, 'Username or password is incorrect')
    context={}
    return render(request, 'login.html', context)