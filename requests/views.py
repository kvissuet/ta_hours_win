from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import Request, Comment
from .forms import RequestForm, CommentForm

def index(request):
	#the home page for ta_hours
	return render(request, 'requests/index.html')
	
def requests(request):
	#show all requests.
	requests = Request.objects.order_by('date_posted')
	context = {'requests': requests}
	return render(request, 'requests/requests.html', context)
	
def new_request(request):
	#post a new request
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form  = RequestForm()
		
	else:
		#POST data submitted; process data.
		form = RequestForm(request.POST)
		if form.is_valid():

			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()

			return HttpResponseRedirect(reverse('requests:comments'))
			
	context = {'form': form}
	return render(request, 'requests/new_request.html', context)
	
def comment(request, request_id):
	"""Show a single topic and all its entries."""
	r = Request.objects.get(id=request_id)
	entries = r.comment_set.order_by('-date_added')
	context = {'request': r, 'entries': entries, 'user':request.user}
	return render(request, 'requests/comments.html', context)
	
@login_required	
def new_comment(request, request_id):
	"""Add a new entry for a particular topic."""
	r = Request.objects.get(id=request_id)
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CommentForm()
	else:
		# POST data submitted; process data.
		form = CommentForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.owner=request.user
			new_entry.request = r
			new_entry.save()
			return HttpResponseRedirect(reverse('requests:comment',
				args=[request_id]))
	context = {'request': r, 'form': form}
	return render(request, 'requests/new_comment.html', context)

@login_required	
def edit_comment(request, comment_id):
	"""Edit an existing entry."""
	comment = Comment.objects.get(id=comment_id)
	r = comment.request
	if comment.owner != request.user:
		raise Http404
	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = CommentForm(instance=comment)
	else:
		# POST data submitted; process data.
		form = CommentForm(instance=comment, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('requests:comment',
					args=[r.id]))
	context = {'comment': comment, 'request': r, 'form': form}
	return render(request, 'requests/edit_comment.html', context)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
