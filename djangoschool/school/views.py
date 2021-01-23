from django.shortcuts import render, redirect  # ดีงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน
from .models import ExamScore
from django.contrib.auth.models import User

# Create your views here.

def HomePage(request):
    #return HttpResponse('<h2> Hello Nawaphong Yoochum </h2>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ContactUs(requate):
    return render(requate, 'school/contactUs.html')

def ShowScore(request):
    score = ExamScore.objects.all() # ดึงค่ามาจาก database ทั้งหมด    [['A', 20], ['B', 40]]
    
    context = {'score':score}

    return render(request, 'school/showscore.html', context)

def Register(request):

    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()

        return redirect('home-page')

    return render(request, ('school/register.html'))

