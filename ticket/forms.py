# application/forms.py
from django import forms
from adminLitreview import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image']


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'content']
