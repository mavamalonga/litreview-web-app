# application/forms.py
from django import forms


class UserFollowsForm(forms.Form):
    username = forms.CharField(max_length=100)
