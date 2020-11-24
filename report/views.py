from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'report/home.html')

def submit(request):
    return render(request,'report/submission.html')

def read(request):
    return render(request,'report/read.html')