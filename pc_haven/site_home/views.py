from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .forms import CreateUserForm, EditUserForm

# Create your views here.
def home(request):
    context = {

    }
    return render(request, "site_home/index.html", context)

def signupPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
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
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect("home")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {

    }

    return render(request, "site_home/loginPage.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def viewProfile(request):
    user = request.user

    context = {
        "user":user
    }

    return render(request, "site_home/viewProfilePage.html", context)

@login_required(login_url="login")
def accountSettings(request):
    user = request.user
    form = EditUserForm(user)
    context = {
        "username": user.username,
        "first_name":user.first_name,
        "last_name": user.last_name,
    }
    return render(request, "site_home/editProfilePage.html", context)
    # return render(request, "site_home/settingsPage.html", context)


@login_required(login_url="login")
def editProfile(request):
    form = EditUserForm()
    context = {
        "form":form
    }
    return render(request, "site_home/editProfilePage.html", context)