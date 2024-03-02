from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Departments,Doctors
from .forms import  BookingForms
# Create your views here.
def user_login(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username = username, password = password)
        if user is not None:
            request.session['username'] = username
            return  redirect(home)
        else:
            messages.error(request,"Bad Creadentails")
            return redirect(user_login)
    return render(request,'login_page.html' )


def user_sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request, "success")
        request.session['username'] = username
        return redirect('home')
    return render(request,'sign_up.html' )


def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(user_login)

def home(request):
    if 'username' in request.session:
        return render(request , 'home.html')
    return redirect(user_login)
def about(request):
    return render(request,"about.html")
def doctors(request): 
    context = { 'doctors': Doctors.objects.all() }
    return render(request,"doctors.html",context)
def booking(request):
    if request.method == "POST":
        form = BookingForms(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForms()
    context = {
        "form" : form
    }
    return render(request,"booking.html",context)
def contact(request):
    return render(request,"contact.html")
def departments(request):
    context = {
        'dept':Departments.objects.all()
    }
    return render(request,"departments.html",context)