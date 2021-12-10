# -/projects/litreview-web-app/litreview/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import application.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/<int:review_id>/delete/', application.views.review_delete, name='review-delete'),
    path('unfollow/<int:link_id>/', application.views.unfollow, name='unfollow'),
    path('follows/', application.views.follows, name='follows'),
    path('ticket/<int:ticket_id>/delete/', application.views.ticket_delete, name='ticket-delete'),
    path('ticket/<int:ticket_id>/update/', application.views.ticket_update, name='ticket-update'),
    path('posts/', application.views.posts, name='posts'),
    path('ticket/<int:ticket_id>/review/', application.views.review, name='review'),
    path('create-review/', application.views.create_review, name='create-review'),
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