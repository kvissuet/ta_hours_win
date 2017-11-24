#Defines URL patterns for requests

from django.conf.urls import url

from . import views

urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),
	
	#Show all requests.
	url(r'^requests/$', views.requests, name='requests'),
]