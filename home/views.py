from django.shortcuts import render, HttpResponse
from home.models import Patient
# Create your views here.
def about(request):
    return render(request, 'about.html')

def administrator(request):
    return render(request, 'administrator.html')

def doctors(request):
    return render(request, 'doctors.html')

#from contacts
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
        #print(name,dob,age,gender)
        ins = Patient(name=name, dob=dob, age=age, gender=gender, email=email, contact=contact, address=address,
                      desc=desc, doctor=doctor, date=date, time=time)
        ins.save()
        print ("The data is submitted to the database")
        #return HttpResponse("Contact Page(/contact)")
    return render(request, 'patient.html')

