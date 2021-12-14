# application/forms.py
from django import forms
from followers import models

class UserFollowsForm(forms.Form):
		username = forms.CharField(max_length=100)
			