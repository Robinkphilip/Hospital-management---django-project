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
            messages.error(request,"Incorrect username or password")
            return redirect(user_login)
    return render(request,'login_page.html' )


def user_sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif username and password and email is not None:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            request.session['username'] = username
            return redirect(home)
        else:
            messages.error(request, "Empty field")
            return redirect('signup')
    return render(request, 'sign_up.html' )


def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(user_login)

def home(request):
    if 'username' in request.session:
        return render(request , 'home.html')
    return redirect(user_login)
def about(request):
    if 'username' in request.session:
        return render(request,"about.html")
    return redirect(user_login)
def doctors(request): 
    if 'username' in request.session:
        context = { 'doctors': Doctors.objects.all() }
        return render(request,"doctors.html",context)
    return redirect(user_login)
def booking(request):
    if 'username' in request.session:
        if request.method == "POST":
            form = BookingForms(request.POST)
            if form.is_valid():
                form.save()
        form = BookingForms()
        context = {
            "form" : form
            }
        return render(request,"booking.html",context)
    return redirect(user_login)
def contact(request):
    if 'username' in request.session:
        return render(request,"contact.html")
    return redirect(user_login)
def departments(request):
    if 'username' in request.session:
        context = {
            'dept':Departments.objects.get(1)
        }
        return render(request,"departments.html",context)
    return redirect(user_login)