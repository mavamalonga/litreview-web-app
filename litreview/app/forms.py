# app/forms.py

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


# s'identifier 
class SignInForm(forms.Form):
	name = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput())

# s'inscrire 
class SignUpForm(forms.Form):
	name = forms.CharField(required=True, max_length=100)
	firstname = forms.CharField(required=True, max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2021)))