from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Students
def index(request):
    return HttpResponse('hello')
def info(request):
    return render(request,'index1.html')
def createstudent(request):
    name=request.POST.get('name')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    stu=Students.create(name,age,gender)
    stu.save()
    stulist=Students.objects.values().filter(sname='lang')
    return render(request,'index2.html',{'student':stulist})
