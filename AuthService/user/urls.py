from django.urls import path
from .views import login, logout, profile, register

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
]