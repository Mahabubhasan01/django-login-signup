from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import sign_up_form
from django.contrib.auth import authenticate, login as logtoin, logout, update_session_auth_hash
# Create your views here.

# Register or sign up view


def sign_up(request):

    if request.method == 'POST':
        fm = sign_up_form(request.POST)
        fm.is_valid()
        fm.save()
        messages.success(request, 'Succesfully created your account')
        fm = sign_up_form()
        messages.success(request, 'Succesfully created your account')
    else:
        fm = sign_up_form(request.POST)
    return render(request, 'auth/signup.html', {'form': fm})

# Login view


def login(request):
    fm = AuthenticationForm(request=request, data=request.POST)
    if not request.user.is_authenticated:
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                logtoin(request, user)
                messages.success(request, 'Login Successfully!!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'auth/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')

# profile view


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'auth/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')
# Logout view


def user_logut(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password succesfully changes!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'auth/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

        #without old password
def change_pass1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password succesfully changes!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'auth/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
