from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *


def home(request):
    return render(request, 'myapp/home.html', {})


def about(request):
    return render(request, 'myapp/about.html', {})


def contact(request):
    return render(request, 'myapp/contact.html', {})


def properties(request):
    return render(request, 'myapp/properties.html', {})


def login(request):
    return render(request, 'myapp/login.html', {})


def signup(request):
    return render(request, 'myapp/signup.html', {})
