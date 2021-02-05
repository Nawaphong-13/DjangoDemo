from typing import Sequence
from django.db.models.base import Model
from django.shortcuts import render, redirect  # ดีงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน
from .models import ALLStudent, ExamScore
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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




################## Search Page ###################################
@login_required  # บังคับ function นี้ต้อง login

def SearchStudent(request):
    # MODELS.objects.all() ดึงค่าทั้งหมด
    # MODELS.objects.get(student_id='63001') ดึงค่าแค่ตัวเดียว หากเกินจะ error
    # MODELS.objects.filter(level='ม.1') ดึงค่าหลายค่า
    #search = ALLStudent.objects.get(student_id=)
    if request.method == 'POST':
        data = request.POST.copy() # Input
        searchid = data.get('search')  # 631001 type 'str'
        print(searchid, type(searchid))
        try:
            result = ALLStudent.objects.get(student_id=searchid)
            print('RESULT :', result)
            context = {'result':result, 'check':'Found'}
        except:
            context = {'result':'ไม่มีข้อมูลในระบบ', 'check':'Notfound'}

        return render(request, 'school/search.html', context)


    return render(request, 'school/search.html')


###################### Edit Profile ###############################
@login_required  # บังคับ function นี้ต้อง login

def EditProfile(request):

    username = request.user.username
    current = User.objects.get(username=username)

    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        # password = data.get('password')

        myprofile = User.objects.get(username=username)
        myprofile.username = email
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.email = email
        #myprofile.set_password(password)
        myprofile.save()
        # from django.shortcuts import redirect
        return redirect('edit-profile')


    context = {'data':current}
    return render(request, ('school/editprofile.html'), context)
