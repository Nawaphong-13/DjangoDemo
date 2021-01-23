from django.shortcuts import render  # ดีงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน
from .models import ExamScore

# Create your views here.

def HomePage(request):
    #return HttpResponse('<h2> Hello Nawaphong Yoochum </h2>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ContactUs(requate):
    return render(requate, 'school/contactUs.html')

def ShowScore(request):
    score = ExamScore.objects.all() # ดึงค่ามาจาก database ทั้งหมด
    
    context = {'score':score}

    return render(request, 'school/showscore.html', context)