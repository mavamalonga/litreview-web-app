# -/projects/litreview-web-app/litreview/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import application.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication.views.login_page, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)