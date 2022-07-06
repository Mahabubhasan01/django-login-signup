from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import sign_up_form
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# Register or sign up view
def sign_up(request):

    if request.method == 'POST':
        fm = sign_up_form(request.POST)
        fm.is_valid()
        fm.save()
        messages.success(request, 'Succesfully created your account')
        fm = sign_up_form()
        messages.success(request,'Succesfully created your account')
    else:
        fm = sign_up_form(request.POST)
    return render(request, 'auth/signup.html', {'form': fm})

# Login view
def login(request):
    fm = AuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data['username']
        password = fm.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            return HttpResponseRedirect('/profile/')
    else:        
        fm = AuthenticationForm()
    return render(request, 'auth/login.html',{'form':fm})

#profile view
def profile(request):
    return render(request,'auth/profile.html')