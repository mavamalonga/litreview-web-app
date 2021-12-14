from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication import forms
from django.conf import settings

from application import forms
from application import models
from authentication.models import User

def get_users_flux(request):
	"""We collect all the users to whom the user is subscribed"""
	users = []
	users_follows = models.UserFollows.objects.filter(user=request.user)
	for user in users_follows:
		users.append(user.followed_user)
	users.append(request.user)
	return users

def get_tickets(request, users):
	"""we collect all the tickets of the users to whom we are subscribed"""
	tickets = []
	for user in users:
		tickets_by_user = models.Ticket.objects.filter(author=user)
		for ticket in tickets_by_user:
			tickets.append(ticket)
	tickets = sorted(tickets, key=lambda k: k.date_created, reverse=True)
	return tickets

def get_reviews(request, users):
	"""we collect all the reveiws of the users to whom we are subscribed"""
	reviews = []
	for user in users:
		review_by_user = models.Review.objects.filter(user=user).order_by('-time_created')
		for review in review_by_user:
			reviews.append(review)
	reviews = sorted(reviews, key=lambda k: k.time_created, reverse=True)
	return reviews


@login_required
def flux(request):
	users = get_users_flux(request)
	tickets = get_tickets(request, users)
	reviews = get_reviews(request, users)
	context = {'tickets': tickets, 'reviews': reviews, 'page_name':'Flux'}
	return render(request, 'application/home.html', context)

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
			return redirect('flux')
	context = {'ticket_form': ticket_form,
		'photo_form': photo_form, 'page_name':'Créer un ticket'}
	return render(request, 'application/create_ticket.html', context=context)

@login_required
def review(request, ticket_id):
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
	return render(request, 'application/review.html', context)

@login_required
def create_review(request):
	ticket_form = forms.TicketForm()
	photo_form = forms.PhotoForm()
	review_form = forms.ReviewForm()
	if request.method == 'POST':
		ticket_form = forms.TicketForm(request.POST)
		photo_form = forms.PhotoForm(request.POST, request.FILES)
		review_form = forms.ReviewForm(request.POST)
		if all([ticket_form.is_valid(), photo_form.is_valid(), review_form.is_valid()]):
			# ticket and photo
			photo = photo_form.save(commit=False)
			photo.uploader = request.user
			photo.save()
			ticket = ticket_form.save(commit=False)
			ticket.author = request.user
			ticket.photo = photo
			ticket.save()
			# review
			review = review_form.save(commit=False)
			review.ticket = ticket
			review.user = request.user
			review.save()
			return redirect('flux')
	context = {'ticket_form': ticket_form, 'photo_form': photo_form,
		'review_form': review_form, 'page_name':'Créer une critique (pas en réponse à un ticket)'}
	return render(request, 'application/create_review.html', context=context)

@login_required
def posts(request):
	"""We collect all the users to whom the user is subscribed"""
	users = []
	users_follows = models.UserFollows.objects.filter(user=request.user)
	for user in users_follows:
		users.append(user.followed_user)
	users.append(request.user)

	"""we collect all the tickets of the users to whom we are subscribed"""
	tickets = []
	for user in users:
		tickets_by_user = models.Ticket.objects.filter(author=user).order_by('-date_created')
		for ticket in tickets_by_user:
			tickets.append(ticket)

	"""we collect all the tickets of the users to whom we are subscribed"""
	tickets = sorted(tickets, key=lambda k: k.date_created, reverse=True)

	"""we collect all the reveiws of the users to whom we are subscribed"""
	reviews = []
	for user in users:
		review_by_user = models.Review.objects.filter(user=user).order_by('-time_created')
		for review in review_by_user:
			reviews.append(review)

	"""we collect all the reviews of the users to whom we are subscribed"""
	reviews = sorted(reviews, key=lambda k: k.time_created, reverse=True)

	context = {'tickets': tickets, 'reviews': reviews, 'page_name': 'Posts'}
	return render(request, 'application/posts.html', context)

@login_required
def ticket_update(request, ticket_id):
	ticket = models.Ticket.objects.get(id=ticket_id)
	ticket_form = forms.TicketForm(instance=ticket)
	photo_form = forms.PhotoForm(instance=ticket.photo)
	if request.method == 'POST':
		ticket_form = forms.TicketForm(request.POST, instance=ticket)
		photo_form = forms.PhotoForm(request.POST, request.FILES, instance=ticket.photo)
		if all([ticket_form.is_valid(), photo_form.is_valid()]):
			photo = photo_form.save(commit=False)
			photo.uploader = request.user
			photo.save()
			ticket = ticket_form.save(commit=False)
			ticket.author = request.user
			ticket.photo = photo
			ticket.save()
			return redirect('posts')
	context = {'ticket_form': ticket_form, 'photo_form':photo_form,
		'page_name':'Ticket update'}
	return render(request, 'application/ticket_update.html', context)

@login_required
def ticket_delete(request, ticket_id):
	ticket = models.Ticket.objects.get(id=ticket_id)
	ticket.delete()
	return redirect('posts')

def review_delete(request, review_id):
	review = models.Review.objects.get(id=review_id)
	review.delete()
	return redirect('posts')

@login_required
def follows(request):
	form = forms.UserFollowsForm()
	followers = models.UserFollows.objects.filter(followed_user=request.user)
	follows = models.UserFollows.objects.filter(user=request.user)
	error = None
	if request.method == 'POST':
		form = forms.UserFollowsForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			if username != f'{request.user}':
				user = User.objects.get(id=request.user.id)
				followed_user = User.objects.filter(username=username)[0]
				if followed_user != None:
					add_follower = models.UserFollows(user=user, followed_user=followed_user)
					add_follower.save()
				else:
					return redirect ('follows')
			else:
				error = 'Désolé vous ne pouvez pas vous auto-abonné'
	context = {'form': form, 'followers': followers,
		'follows': follows, 'page_name': 'Abonnements', 'error': error}
	return render(request, 'application/follows.html', context=context)

@login_required
def unfollow(request, link_id):
	link = models.UserFollows.objects.get(id=link_id)
	link.delete()
	return redirect('follows')




