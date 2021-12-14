from django.db import models
from django.conf import settings

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

