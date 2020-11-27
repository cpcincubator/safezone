from django.shortcuts import render, redirect

from .models import Report,Contact
# Create your views here.

def home(request):
    return render(request,'report/home.html')

def submit(request):
    if request.method == 'POST':
        report_type=request.POST["report_type"]
        date = request.POST["date"]
        location = request.POST["location"]
        time= request.POST["time"]
        report_title=request.POST["report_title"]
        description=request.POST["description"]
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]

        report=Report(report_type=report_type,date=date,location=location,time=time,report_title=report_title,description=description)
        report.save()
        contact=Contact(name=name,email=email,phone=phone)
        contact.save()
        return redirect("home")
    
    context={}
    return render(request,'report/submission.html',context)

def read(request):
    return render(request,'report/read.html')