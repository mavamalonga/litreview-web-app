# -/projects/litreview-web-app/litreview/urls.py

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', views.connexion),
]
