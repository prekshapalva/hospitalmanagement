from django.shortcuts import render, HttpResponse
from home.models import Patient, Doctor
# Create your views here.
def about(request):
    return render(request, 'about.html')

def administrator(request):
    return render(request, 'administrator.html')

def doctors(request):
    return render(request, 'doctors.html')

def patient_main(request):
    return render(request, 'patient_main.html')


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
        #print(name,dob,age,gender)
        ins = Doctor(doc_name=doc_name, doc_degree=doc_degree, doc_dob=doc_dob, doc_age=doc_age,
                     doc_gender=doc_gender, doc_email=doc_email,
                doc_contact=doc_contact,doc_address=doc_address,
                    )
        ins.save()
        print ("The data is submitted to the database")
        #return HttpResponse("Contact Page(/contact)")
    return render(request, 'add_doctor_by_admin.html')

