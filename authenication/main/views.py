from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from main.forms import Signup,EditForm,PasswordChange
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have logged in'))
            return redirect('/')
        else:
            messages.success(request,('Error in login. PLease try with correct username and password'))
            return redirect('login')
    else:
        return render(request,'main/login.html')
def logout_user(request):
    logout(request)
    messages.success(request,('You have been logout'))
    return redirect('login')

def register_user(request):
    if request.method=="POST":
        form=Signup(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,('You Registered Successfully!'))
            return redirect('/')

    else:
        form=Signup()
    context={'form':form}
    return render(request,'main/reg.html',context)
def edit_profile(request):
    if request.method=="POST":
        form=EditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('Your Details Added Successfully!'))
            return redirect('/')
    else:
        form=EditForm(instance=request.user)
    context={'form':form}
    return render(request,'main/edit.html',context)
        
def update_password(request):
    if request.method=="POST":
        form=PasswordChange(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('Your Details Added Successfully!'))
            return redirect('/')
    else:
        form=PasswordChange(user=request.user)
    context={'form':form}
    return render(request,'main/password_update.html',context)
    