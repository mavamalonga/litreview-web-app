from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication import forms
from django.conf import settings

from application import forms
from application import models
from authentication.models import User

@login_required
def home(request):
	tickets = models.Ticket.objects.all()
	reviews = models.Review.objects.all()
	# id: toto, pwd: Se3cret!
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
			return redirect('home')
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
			return redirect('home')
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
			return redirect('home')
	context = {'ticket_form': ticket_form, 'photo_form': photo_form,
		'review_form': review_form, 'page_name':'Créer une critique (pas en réponse à un ticket)'}
	return render(request, 'application/create_review.html', context=context)

def posts(request):
	posts = models.Ticket.objects.filter(author=request.user.id)
	reviews = models.Review.objects.filter(user=request.user.id)
	context = {'posts': posts, 'reviews': reviews, 'page_name': 'Posts'}
	return render(request, 'application/posts.html', context)

def ticket_update(request, ticket_id):
	ticket = models.Ticket.objects.get(id=ticket_id)
	form = forms.TicketForm(instance=ticket)
	if request.method == 'POST':
		form = forms.TicketForm(request.POST, instance=ticket)
		if form.is_valid():
			ticket = form.save()
			return redirect('posts')
	context = {'form': form, 'page_name':'Ticket update'}
	return render(request, 'application/ticket_update.html', context)

def ticket_delete(request, ticket_id):
	ticket = models.Ticket.objects.get(id=ticket_id)
	if request.POST == 'POST':
		ticket.delete()
		return redirect('posts')
	context = {'page_name':'Ticket delete'}
	return render(request, 'application/ticket_delete.html', context)

def follows(request):
	form = forms.UserFollowsForm()
	followers = models.UserFollows.objects.filter(followed_user=request.user)
	follows = models.UserFollows.objects.filter(user=request.user)
	if request.method == 'POST':
		form = forms.UserFollowsForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			user = User.objects.get(id=request.user.id)
			followed_user = User.objects.filter(username=username)[0]
			if followed_user != None:
				add_follower = models.UserFollows(user=user, followed_user=followed_user)
				add_follower.save()
			else:
				return redirect ('follows')
	return render(request, 'application/follows.html', context={'form': form, 'followers': followers,
		'follows': follows, 'page_name': 'Abonnements'})

def unfollow(request, link_id):
	link = models.UserFollows.objects.get(id=link_id)
	link.delete()
	return redirect('follows')




