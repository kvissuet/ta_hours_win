from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['title', 'date', 'time', 'room', 'course', 'value']
		labels = {'title' : 'Title', 'date' : 'Date', 'time' : 'Time', 'room' : 'Room', 'course' : 'Course', 'value' : 'value'}
		