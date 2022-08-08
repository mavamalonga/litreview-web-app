from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from adminLitreview import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('date_joined', 'groups')
    search_fields = ('username', )


@admin.register(models.UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')
    list_filter = ('user', )
    search_fields = ('user', )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'uploader', 'date_created')
    list_filter = ('title', 'uploader', 'date_created')
    search_fields = ('uploader', 'title')


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time_created')
    list_filter = ('title', 'author', 'time_created')
    search_fields = ('author', 'title')


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline', 'time_created')
    list_filter = ('user', 'headline', 'time_created')
    search_fields = ('user', 'time_created')
