# application/forms.py
from django import forms
from application import models

class PhotoForm(forms.ModelForm):
	class Meta:
		model = models.Photo
		fields = ['image']

class TicketForm(forms.ModelForm):
	class Meta:
		model = models.Ticket
		fields = ['title', 'content']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = models.Review
		fields = ['headline', 'rating', 'body']

class UserFollowsForm(forms.Form):
		username = forms.CharField(max_length=100)
			