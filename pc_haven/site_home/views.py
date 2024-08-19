from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .forms import CreateUserForm

# Create your views here.
def home(request):
    context = {

    }
    return render(request, "site_home/index.html", context)

def signupPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            messages.success(request, "Account created for " + user)
            return redirect("login")
    context = {
        "form": form 
    }
    return render(request, "site_home/signupPage.html", context)

def loginPage(request):
    context = {

    }
    return render(request, "site_home/loginPage.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")