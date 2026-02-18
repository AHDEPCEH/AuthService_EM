from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return HttpResponse("User created")

def login(request):
    return HttpResponse("User successful login")

def logout(request):
    return HttpResponse("User successful logout")

def profile(request):
    return HttpResponse("User's profile")

