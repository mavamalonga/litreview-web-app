# application/forms.py
from django import forms
from review import models

class ReviewForm(forms.ModelForm):
	class Meta:
		model = models.Review
		fields = ['headline', 'rating', 'body']
