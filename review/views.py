from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication import forms
from django.conf import settings

from review import forms
from adminLitreview import models


@login_required
def create_review(request, ticket_id):
	ticket = models.Ticket.objects.get(id=ticket_id)
	form = forms.ReviewForm()
	if request.method == 'POST':
		form = forms.ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.ticket = ticket
			review.user = request.user
			review.save()
			return redirect('flux')
	context = {'form': form, 'ticket':ticket, 'page_name':'Créer une critique'}
	return render(request, 'review/create_review.html', context)

def delete_review(request, review_id):
	review = models.Review.objects.get(id=review_id)
	review.delete()
	return redirect('posts')

