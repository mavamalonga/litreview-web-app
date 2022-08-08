# application/forms.py
from django import forms
from adminLitreview import models

class UserFollowsForm(forms.Form):
		username = forms.CharField(max_length=100)
			