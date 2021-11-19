# -/projects/litreview-web-app/app/views.py

from django.shortcuts import render
from app.forms import SignInForm, SignUpForm

def signIn(request):
	form = SignInForm()
	return render(request, 'app/signIn.html', {'form': form})

def signUp(request):
	form = SignUpForm()
	return render(request, 'app/signUp.html', {'form':form})
