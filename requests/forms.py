from django import forms
from .models import Request, Comment

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['title', 'date', 'time', 'room', 'course', 'value']
		labels = {'title' : 'Title', 'date' : 'Date', 'time' : 'Time', 'room' : 'Room', 'course' : 'Course', 'value' : 'value'}
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}