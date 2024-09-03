from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin



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
    return render(request, "site_home/signup.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
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

    return render(request, "site_home/login.html", context)

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
    form = EditUserForm(instance=request.user)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "username": user.username,
        "first_name":user.first_name,
        "last_name": user.last_name,
        "form": form
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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'site_home/password_reset.html'
    email_template_name = 'site_home/password_reset_email.html'
    subject_template_name = 'site_home/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')