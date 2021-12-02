from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication import forms
from django.conf import settings

from application import forms
from application import models

@login_required
def home(request):
	tickets = models.Ticket.objects.all()
	# id: toto, pwd: Se3cret!
	return render(request, 'application/home.html', {'tickets': tickets})

@login_required
def create_ticket(request):
	ticket_form = forms.TicketForm()
	photo_form = forms.PhotoForm()
	if request.method == 'POST':
		ticket_form = forms.TicketForm(request.POST)
		photo_form = forms.PhotoForm(request.POST, request.FILES)
		if all([ticket_form.is_valid(), photo_form.is_valid()]):
			photo = photo_form.save(commit=False)
			photo.uploader = request.user
			photo.save()
			ticket = ticket_form.save(commit=False)
			ticket.author = request.user
			ticket.photo = photo
			ticket.save()
			return redirect('home')
	context = {'ticket_form': ticket_form,
		'photo_form': photo_form}
	return render(request, 'application/create_ticket.html', context=context)


