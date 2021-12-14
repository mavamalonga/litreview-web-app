# -/projects/litreview-web-app/litreview/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import application.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_user, name='login'),
    path('login/', authentication.views.login_user, name='login'),
    path('sign-up/', authentication.views.signup, name='sign-up'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('flux/', application.views.flux, name='flux'),
    path('posts/', application.views.posts, name='posts'),
    path('create-ticket/', application.views.create_ticket, name='create-ticket'),
    path('create-ticket&review/', application.views.create_ticket_and_review, name='create-ticket-review'),
    path('ticket/<int:ticket_id>/update/', application.views.update_ticket, name='update-ticket'),
    path('ticket/<int:ticket_id>/delete/', application.views.delete_ticket, name='delete-ticket'),
    path('ticket/<int:ticket_id>/create-review/', application.views.create_review, name='create-review'),
    path('review/<int:review_id>/delete/', application.views.delete_review, name='delete-review'),
    path('follows/', application.views.follows, name='follows'),
    path('unfollow/<int:link_id>/', application.views.unfollow, name='unfollow'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)