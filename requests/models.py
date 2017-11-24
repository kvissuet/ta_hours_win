from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Request(models.Model):
	#A request for covering hours
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	room = models.CharField(max_length=200)
	course = models.CharField(max_length=200)
	value = models.CharField(max_length=200)
	date_posted = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
	
	def __str__(self):
		#return a string representation of the request
		return self.title
	
	
class Comment(models.Model):
	"""Something specific learned about a topic"""
	request = models.ForeignKey(Request)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
	class Meta:
		verbose_name_plural = 'comments'

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text[:500] + "..."