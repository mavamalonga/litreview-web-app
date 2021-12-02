from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication import forms
from django.conf import settings

from application import forms
from application import models

@login_required
def home(request):
	# id: toto, pwd: Se3cret!
	return render(request, 'application/home.html')

