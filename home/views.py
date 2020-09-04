from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def about(request):
    return render(request, 'about.html')

def administrator(request):
    context = {'name':'preksha','course':'django'}
    return render(request, 'administrator.html', context)

def doctors(request):
    return render(request, 'doctors.html')

def patients(request):
    return render(request, 'patients.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        query = request.POST['query']
        #print(name,phone,email_id,query)
        ins = Contact(name=name, phone=phone, email=email ,query=query )
        ins.save()
        print ("The data is submitted to the database")
    #return HttpResponse("Contact Page(/contact)")
    return render(request, 'contact.html')

