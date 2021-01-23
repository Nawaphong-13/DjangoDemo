from django.shortcuts import render  # ดีงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน

# Create your views here.

def HomePage(request):
    #return HttpResponse('<h2> Hello Nawaphong Yoochum </h2>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')
