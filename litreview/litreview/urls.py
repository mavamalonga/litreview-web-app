# -/projects/litreview-web-app/litreview/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import application.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-ticket/', application.views.create_ticket, name='create-ticket'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('', authentication.views.login_page, name='login'),
    path('login/', authentication.views.login_page, name='login'),
    path('sign-up/', authentication.views.signup_page, name='sign-up'),
    path('home/', application.views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)