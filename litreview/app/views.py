# -/projects/litreview-web-app/app/views.py

from django.shortcuts import render

def connexion(request):
	return render(request, 'app/connexion.html')
