from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
import datetime as dt
from .models import Patient, Doctor, Notifications,ModelReport
from django.core.mail import EmailMessage
from django.shortcuts import redirect


def getmatchingdoctor():
    doctors = Doctor.objects.all().order_by('numberofpatients')
    doctor_to_return = doctors[0]
    doctor_to_return.numberofpatients += 1
    doctor_to_return.save()
    return doctor_to_return


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def index(request):
    return render(request, 'mainapp/HomePage.html')


def loginUser(request):
    context = {'error': 'Wrong Username or Password'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('mainapp:dashboard'))
        else:
            return render(request, 'mainapp/login.html', context)
    else:
        return render(request, 'mainapp/login.html')


# Add the radio button to get the type of user in both the html and the func below

def RegUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')
        try:
            new_user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                      user_type=usertype)
            login(request, new_user)
            return HttpResponseRedirect(reverse('mainapp:completeaccount'))
        except:
            return render(request, 'mainapp/signup.html', {'isfail': True})
    else:
        return render(request, 'mainapp/signup.html', {'isfail': False})


@login_required
def completeaccount(request):
    if request.method == 'GET':
        if request.user.user_type == 'Patient':
            return render(request, 'mainapp/patientcompleteaccount.html')
        elif request.user.user_type == 'Doctor':
            return render(request, 'mainapp/doctorcompleteaccount.html')
        else:
            return HttpResponseRedirect(reverse('mainapp:reguser'))

    elif request.method == 'POST':
        if request.user.user_type == 'Patient':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            address = request.POST.get('address', default=None)
            phonenumber = request.POST.get('phonenumber', default=None)
            dateofbirth = request.POST.get('dateofbirth')
            age = dt.datetime.now().year - int(dateofbirth[0:4])
            sex = request.POST.get('sex')
            user = request.user
            patient_obj = Patient(user=user, firstname=firstname, lastname=lastname, dateofbirth=dateofbirth,
                                  address=address, phonenumber=phonenumber, age=age, sex=sex)
            if patient_obj:
                patient_obj.doctor = getmatchingdoctor()
                em=patient_obj.doctor.user.email
                body="{} is now your patient! ".format(patient_obj.user.username)
                mel=EmailMessage("New Patient",body,to=[em])
                mel.send()
                patient_obj.save()
                return HttpResponseRedirect(reverse('mainapp:dashboard'))
            else:
                return HttpResponseRedirect(reverse('mainapp:reguser'))

        elif request.user.user_type == 'Doctor':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            phonenumber = request.POST.get('phonenumber', default=None)
            user = request.user
            degrees = request.POST.get('degrees')
            registrationno = request.POST.get('registrationno')
            bio = request.POST.get('bio')
            doctor_obj = Doctor(user=user, firstname=firstname, lastname=lastname, phonenumber=phonenumber,
                                degrees=degrees, registrationno=registrationno, bio=bio)
            if doctor_obj:
                doctor_obj.save()
                return HttpResponseRedirect(reverse('mainapp:dashboard'))
            else:
                return HttpResponseRedirect(reverse('mainapp:reguser'))
    else:
        return HttpResponseRedirect(reverse('mainapp:reguser'))


@login_required
def UpdateUser(request):
    if request.method == 'POST':
        if request.user.user_type == 'Doctor':
            user = request.user
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            phonenumber = request.POST.get('phone')
            degrees = request.POST.get('degrees')
            iscert = request.POST.get('certification')
            regno = request.POST.get('regno')
            bio = request.POST.get('bio')
            doc = Doctor.objects.get(user=request.user)
            doc.user = user
            doc.firstname = firstname
            doc.lastname = lastname
            doc.phonenumber = phonenumber
            doc.degrees = degrees
            if iscert == 'YES':
                iscert = True
            else:
                iscert = False
            doc.iscertified = iscert
            doc.registrationno = regno
            doc.bio = bio
            doc.save()
            return HttpResponseRedirect(reverse('mainapp:dashboard'))
        elif request.user.user_type == 'Patient':
            user = request.user
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            dob = request.POST.get('dob')
            address = request.POST.get('addr')
            sex = request.POST.get('sex')
            phonenumber = request.POST.get('phone')
            pat = Patient.objects.get(user=user)
            pat.user = user
            pat.firstname = firstname
            pat.lastname = lastname
            pat.phonenumber = phonenumber
            pat.dateofbirth = dob
            pat.age = dt.datetime.now().year - int(dob[0:4])
            pat.address = address
            pat.sex = sex
            pat.save()
            return HttpResponseRedirect(reverse('mainapp:dashboard'))
    if request.method == 'GET':
        if request.user.user_type == 'Doctor':
            docdata = Doctor.objects.get(user=request.user)
            return render(request, 'mainapp/doctorUpdate.html', {'data': docdata})
        elif request.user.user_type == 'Patient':
            user = request.user
            patdata = Patient.objects.get(user=user)
            return render(request, 'mainapp/patientUpdate.html', {'data': patdata})
    else:
        return HttpResponseRedirect(reverse('mainapp:reguser'))


@login_required
def dash(request):
    context = {'usertype': request.user.username}
    if request.user.user_type == 'Patient':
        return render(request, 'mainapp/Dashboard.html', {'usertype': request.user.username})
    elif request.user.user_type == 'Doctor':
        doc = Doctor.objects.get(user=request.user)
        docNotif = Notifications.objects.filter(doctor=doc)
        docNotif = docNotif.filter(hasNotification=True)
        if docNotif:
            context['notif'] = 'You have new notifications'
        return render(request, 'mainapp/DashboardTwo.html', context)
    else:
        return HttpResponseRedirect(reverse('mainapp:reguser'))


@login_required
def account(request):
    if request.user.user_type == 'Doctor':
        doc = Doctor.objects.get(user=request.user)
        return render(request, 'mainapp/detailDoctor.html', {'data': doc})
    elif request.user.user_type == 'Patient':
        pat = Patient.objects.get(user=request.user)
        return render(request, 'mainapp/detailPatient.html', {'data': pat})
    else:
        return HttpResponseRedirect(reverse('mainapp:reguser'))


@login_required
def notif(request):
    if request.user.user_type != 'Doctor':
        return HttpResponseRedirect(reverse('mainapp:userlogin'))
    else:
        doc = Doctor.objects.get(user=request.user)
        docNotif = Notifications.objects.filter(doctor=doc)
        res = []
        for notif in docNotif:
            notif.hasNotification = False
            res.append(notif.patient.user.username)
            notif.save()
        k = list(set(res))
    print(k)
    return render(request, 'mainapp/Notification.html', {'k': k})

def mail(request):
    if request.method == 'POST':
        if request.user.user_type == 'Patient':
            pat = Patient.objects.get(user=request.user)
            docEmail = pat.doctor.user.email
            body = request.POST.get('body')
            email = EmailMessage('Medical Report', body, to=[docEmail])
            email.send()
            return HttpResponseRedirect(reverse('mainapp:dashboard'))
        if request.user.user_type == 'Doctor':
            doc = Doctor.objects.get(user=request.user)
            patEmail = request.POST.get('emailauth')
            body = request.POST.get('body')
            email = EmailMessage('Medical Report: Reply', body, to=[patEmail])
            email.send()
            return HttpResponseRedirect(reverse('mainapp:dashboard'))
    if request.method == 'GET':
        if request.user.user_type == 'Patient':
            return render(request, 'mainapp/PatientEmail.html')
        if request.user.user_type == 'Doctor':
            doc = Doctor.objects.get(user=request.user)
            patients = Patient.objects.filter(doctor= doc)
            return render(request, 'mainapp/DoctorEmail.html', {'patients':patients})


@login_required
def viewreport(request):
    if request.user.user_type == 'Doctor':
        doc = Doctor.objects.get(user=request.user)
        modelreportqueryset=ModelReport.objects.filter(patient__doctor=doc)
        return render(request,'mainapp/doctorreportlist.html',{'objectlist':modelreportqueryset})
    elif request.user.user_type == 'Patient':
        pat = Patient.objects.get(user=request.user)
        modelreportqueryset=ModelReport.objects.filter(patient=pat)
        return render(request,'mainapp/patientreportlist.html',{'objectlist':modelreportqueryset})

@login_required
def viewreportdetail(request,pk):
    if request.user.user_type == 'Patient' or request.user.user_type == 'Doctor':
        modelreport=ModelReport.objects.get(pk=pk)
        modelreport=modelreport.report_content
        modelreport=eval(modelreport)
        for val in modelreport:
            modelreport[val]=modelreport[val][0]
        return render(request,'mainapp/reportdetail.html',{'object':modelreport})
    else:
        return HttpResponseRedirect(reverse('mainapp:reguser'))
