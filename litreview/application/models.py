from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class UserFollows(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name='following')
	followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name='followed_by')
"""
	class Meta:
		unique_together = ('user', 'followed__user',)

"""
class Photo(models.Model):
	image = models.ImageField()
	uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
	photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
	title = models.CharField(max_length=128)
	content = models.TextField(max_length=5000)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title 

class Review(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), 
		MaxValueValidator(5)])
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	headline = models.CharField(max_length=128)
	body = models.TextField(max_length=8192, blank=True)
	time_created = models.DateTimeField(auto_now_add=True)

