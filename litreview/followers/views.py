from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication import forms
from django.conf import settings

from followers import forms
from followers import models
from authentication.models import User


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
				try:
					user = User.objects.get(id=request.user.id)
					followed_user = User.objects.filter(username=username)[0]
					if followed_user != None:
						add_follower = models.UserFollows(user=user, followed_user=followed_user)
						add_follower.save()
					else:
						return redirect ('follows')
				except Exception as e:
					form = forms.UserFollowsForm()
					error = "Désolé ce compte utilisateur n'exsite pas"
			else:
				error = 'Désolé vous ne pouvez pas vous auto-abonné'
	context = {'form': form, 'followers': followers,
		'follows': follows, 'page_name': 'Abonnements', 'error': error}
	return render(request, 'followers/follows.html', context=context)

@login_required
def unfollow(request, link_id):
	link = models.UserFollows.objects.get(id=link_id)
	link.delete()
	return redirect('follows')


