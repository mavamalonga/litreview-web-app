# application/forms.py
from django import forms
from adminLitreview import models

class ReviewForm(forms.ModelForm):
	class Meta:
		model = models.Review
		fields = ['headline', 'rating', 'body']
