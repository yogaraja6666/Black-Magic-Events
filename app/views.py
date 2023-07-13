from typing import Any, Optional
from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import feedback
from app.models import *
from app.form import CustomUserForm,EditUserProfileForm,ProfileUpdateForm,PasswordChangeingForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from qrcode import *
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail


class editprofile(SuccessMessageMixin, generic.UpdateView):
        form_class = EditUserProfileForm
        template_name = 'profileupdate.html'
        success_url = reverse_lazy('updateprofile')
        success_message = 'Profile Updated Successfully'
        def get_object(self):
            return self.request.user
        

class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class  = PasswordChangeingForm
    success_url = reverse_lazy('updateprofile')
    success_message = 'Password Changed Successfully'

def about(request):
    return render(request,'about.html')

def anirudhevent(request):
    lttsevennt1 = levent1.objects.all()
    return render(request,'anirudhevent.html',{'lttsevent1':lttsevennt1})

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fpnumber = request.POST.get('phone')
        fmsg = request.POST.get('message')
        a = feedback(name=fname,email=femail,phonenumber=fpnumber,message=fmsg)
        a.save()
    else:
        print("contact form Post method not work")

    return render(request,'contact.html')

def event(request):
    lttsevent1 = levent1.objects.all()
    lttsevent2 = levent2.objects.all()
    lttsevent3 = levent3.objects.all()
    lttsevent4 = levent4.objects.all()
    upcevent1 = uevent1.objects.all()
    upcevent2 = uevent2.objects.all()
    upcevent3 = uevent3.objects.all()
    upcevent4 = uevent4.objects.all()
    context = {
        'lttsevent1':lttsevent1,
        'lttsevent2':lttsevent2,
        'lttsevent3':lttsevent3,
        'lttsevent4':lttsevent4,
        'upcevent1':upcevent1,
        'upcevent2':upcevent2,
        'upcevent3':upcevent3,
        'upcevent4':upcevent4,
    }
    return render(request,'event.html',context)

def general(request):
    if request.method == 'POST':
        ftq = request.POST.get('a')
        print(ftq)
        ftp = 500 * int(ftq)
        general_data = generalcart(user=request.user, ticketqty=ftq,ticketprice=ftp)
        general_data.save()
        return redirect('cart')
    else:
        print('general post method not work')
    lttsevennt1 = levent1.objects.all()   
    return render(request,'general.html',{'lttsevent1':lttsevennt1})

def gold(request):
    if request.method == 'POST':
        ftq = request.POST.get('a')
        print(ftq)
        ftp = 1000 * int(ftq)
        gold_data = goldcart(user=request.user,ticketqty=ftq,ticketprice=ftp)
        gold_data.save()
        return redirect('cart')
    else:
        print('gold post method not work')

    lttsevennt1 = levent1.objects.all()
    return render(request,'gold.html',{'lttsevent1':lttsevennt1})

def home(request):
    lttsevennt1 = levent1.objects.all()
    return render(request,'home.html',{'lttsevent1':lttsevennt1})

def join(request):
    form = CustomUserForm
    if request.method == 'POST':
        form =CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registraion Success You Can Login now..!')    
            return redirect('/login')
    return render(request,'join.html',{'form':form})

def login_page(request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            if request.method == 'POST':
                name = request.POST.get('username')
                pwd = request.POST.get('password')
                user=authenticate(request,username=name,password=pwd)
                if user is not None:
                    login(request,user)
                    return redirect("/")
                else:
                    messages.error(request,'Invalid Username or Password')
                    return redirect("/login")   
            return render(request,'account/login.html',)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect("/")   

def platinum(request):
    if request.method == 'POST':
        ftq = request.POST.get('a')
        print(ftq)
        ftp = 1500 * int(ftq)
        platinum_data = platinumcart(user=request.user,ticketqty=ftq,ticketprice=ftp)
        platinum_data.save()
        return redirect('cart')
    else:
        print('platinum post method not work')
    lttsevennt1 = levent1.objects.all()    
    return render(request,'platinum.html',{'lttsevent1':lttsevennt1})

def cart(request):
    a = platinumcart.objects.filter(user=request.user.id,ispaid=False)
    b = goldcart.objects.filter(user=request.user.id,ispaid=False)
    c = generalcart.objects.filter(user=request.user.id,ispaid=False)
    return render(request,'cart.html',{'a':a,'b':b,'c':c})

def orders(request):
    a = platinumcart.objects.filter(user=request.user.id,ispaid=True)
    b = goldcart.objects.filter(user=request.user.id,ispaid=True)
    c = generalcart.objects.filter(user=request.user.id,ispaid=True)

    return render(request,'myorders.html',{'a':a,'b':b,'c':c})

def platinumpaid(request, id):
    messages.success(request,'Ticket Booked Succesfully')
    a = platinumcart.objects.get(id=id)
    a.ispaid = True
    a.save()
    return redirect('myorders')

def goldpaid(request, id):
    messages.success(request,'Ticket Booked Succesfully')
    b = goldcart.objects.get(id=id)
    b.ispaid = True
    b.save()
    return redirect('myorders')

def generalpaid(request, id):
    messages.success(request,'Ticket Booked Succesfully')
    c = generalcart.objects.get(id=id)
    c.ispaid = True
    c.save()
    return redirect('myorders')

def deleteplatinumcartdata(request, id):
    a = platinumcart.objects.get(id=id)
    a.delete()
    return redirect('cart')
    
def deletegoldcartdata(request,id):
    b = goldcart.objects.get(id=id)
    b.delete()
    return redirect('cart')

def deletegeneralcartdata(request,id):
    c = generalcart.objects.get(id=id)
    c.delete()
    return redirect('cart')