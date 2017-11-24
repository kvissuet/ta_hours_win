from django.db import models

class Request(models.Model):
	#A request for covering hours
	title = models.CharField(max_length=200)
	date = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	room = models.CharField(max_length=200)
	course = models.CharField(max_length=200)
	value = models.CharField(max_length=200)
	date_posted = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		#return a string representation of the request
		return self.title
	
	
