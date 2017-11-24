#Defines URL patterns for requests

from django.conf.urls import url

from . import views

urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),
	
	#Show all requests.
	url(r'^requests/$', views.requests, name='requests'),
	
	#page for adding a new request
	url(r'^new_request/$', views.new_request, name='new_request'),
	
	# Detail page for a single topic
	url(r'^requests/(?P<request_id>\d+)/$', views.comment, name='comment'),
]