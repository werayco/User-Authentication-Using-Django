from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from .forms import UserRegform
from django.urls import reverse
# Create your views here.


def loginer(request):
    formoBJ = AuthenticationForm()
    if request.method == "POST":
        dats = AuthenticationForm(request,request.POST)
        if dats.is_valid():
            user = dats.get_user()
            if user is not None:
                login(request,user)
                return redirect(reverse("homepage"))
    dummy = {"former":formoBJ}
    return render(request,"accnts/login.html",dummy)

def signer(request):
    form = UserRegform()

    if request.method == "POST":
        form = UserRegform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))

    return render(request,"accnts/sign_up.html",{"former":form})


def logouter(request):
    logout(request)
    return redirect("homepage")
