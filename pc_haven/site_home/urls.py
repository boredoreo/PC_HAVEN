from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signupPage, name="signup"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("account/", views.accountSettings, name="settings"),
    path("profile/", views.viewProfile, name="profile"),
    path("edit_profile/", views.editProfile, name="edit_profile")

]