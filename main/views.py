from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .filters import PatientFilter
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# PatientFilter = OrderFilter

# Create your views here
#A view function, or view for short, is a Python function that takes a Web request and returns a Web response. 
#This response can be the HTML contents of a Web page, or a redirect,or anything,

def login(request):
    if request.user.is_authenticated:               #if the details of the user are authenticated
        return redirect('/')                        #it sends user to the dashboard
    else:                                           #else it will 
        if request.method == 'POST':                #this login form is returned using the post method  
            username = request.POST['username']      
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')                #if user authenticated, sends user to the dashboard
            else:                                   #else gives an error 
                messages.error(request, 'Invalid username or password')
                return redirect('login')            #sends to the login page 
        else:
            return render(request, 'main/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')




def dashboard(request):
    patients = Patient.objects.all()                                
    patient_count = patients.count()
    patients_recovered = Patient.objects.filter(status="Recovered") #taking data from the backend 
    patients_deceased = Patient.objects.filter(status="Deceased")   
    deceased_count = patients_deceased.count()
    recovered_count = patients_recovered.count()
    beds = Bed.objects.all()
    beds_available = Bed.objects.filter(occupied=False).count()     #defining the beds available as occupied=false
    context = {                                      # A context is a variable name -> variable value mapping that is passed to a template.
        'patient_count': patient_count,              # Context processors let you specify a number of variables that get set in each context automatically – 
        'beds_available': beds_available,            # -without you having to specify the variables in each render() call.
        'recovered_count': recovered_count,
        'deceased_count':deceased_count,
        'beds':beds
    }
    print(patient_count)       
    return render(request, 'main/dashboard.html', context)          #all this data to be stored in dashboard with respective variable names

def add_patient(request):                                           #here we are adding the details of the patients for the first time
    beds = Bed.objects.filter(occupied=False)                       #filtering the beds available by occupancy false
    doctors = Doctor.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        patient_relative_name = request.POST['patient_relative_name']
        patient_relative_contact = request.POST['patient_relative_contact']
        address = request.POST['address']
        symptoms = request.POST['symptoms']
        prior_ailments = request.POST['prior_ailments']
        bed_num_sent = request.POST['bed_num']                       #creating new variables for existing data and using the POST method to
        bed_num = Bed.objects.get(bed_number=bed_num_sent)           #using .get here as this field will not be defined by the operator nor will it be updated once defined by doctor/staff
        dob = request.POST['dob']
        status = request.POST['status']
        doctor = request.POST['doctor']
        doctor = Doctor.objects.get(name=doctor)
        print(request.POST)
        patient = Patient.objects.create(
            name = name,
        phone_num = phone_num,
        patient_relative_name = patient_relative_name,
        patient_relative_contact = patient_relative_contact, 
        address = address, 
        symptoms = symptoms, 
        prior_ailments = prior_ailments, 
        bed_num = bed_num,
        dob = dob, 
        doctor=doctor,
        status = status
        )
        patient.save()

        bed = Bed.objects.get(bed_number=bed_num_sent)
        bed.occupied = True
        bed.save()
        id = patient.id                              #defining id to be used for the uniqueness of the patient
        return redirect(f"/patient/{id}")
        
    context = {
        'beds': beds,
        'doctors': doctors
    }
    return render(request, 'main/add_patient.html', context)    #all this data beung rendered to the add_patient.html page

def patient(request, pk):                            #this patient page will display data entered from add patients and will be used to update detials 
    patient = Patient.objects.get(id=pk)             #pk means primary key which is used here for uniqueness
    if request.method == "POST":
        doctor = request.POST['doctor']
        doctor_time = request.POST['doctor_time']
        doctor_notes = request.POST['doctor_notes']
        mobile = request.POST['mobile']
        mobile2 = request.POST['mobile2']
        relativeName = request.POST['relativeName']
        address  = request.POST['location']
        print(doctor_time)
        print(doctor_notes)
        status = request.POST['status']
        doctor = Doctor.objects.get(name=doctor)              
        print(doctor)
        patient.phone_num = mobile
        patient.patient_relative_contact = mobile2
        patient.patient_relative_name = relativeName
        patient.address = address
        patient.doctor = doctor
        patient.doctors_visiting_time = doctor_time
        patient.doctors_notes = doctor_notes
        print(patient.doctors_visiting_time)
        print(patient.doctors_notes)
        patient.status = status
        patient.save()
    context = {
        'patient': patient
    }
    return render(request, 'main/patient.html', context)


def patient_list(request):          #here in the pateints list we are using filters so that they can be searched by some value or variable name
    patients = Patient.objects.all()

    # filtering
    myFilter = PatientFilter(request.GET, queryset=patients)

    patients = myFilter.qs
    context = {
        'patients': patients,
        'myFilter': myFilter
    }

    return render(request, 'main/patient_list.html', context)   #will return the page with filtered results if available 

'''
def autocomplete(request):
    if patient in request.GET:
        name = Patient.objects.filter(name__icontains=request.GET.get(patient))
        name = ['js', 'python']
        
        names = list()
        names.append('Shyren')
        print(names)
        for patient_name in name:
            names.append(patient_name.name)
        return JsonResponse(names, safe=False)
    return render (request, 'main/patient_list.html')
'''

def autosuggest(request):                           #auto suggests patient id  
    query_original = request.GET.get('term')
    queryset = Patient.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def autodoctor(request):                            #suggests name of doctor by itself 
    query_original = request.GET.get('term')
    queryset = Doctor.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

def info(request):
    return render(request, "main/info.html") #will send user to the info page