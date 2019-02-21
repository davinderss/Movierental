from django.contrib.auth.models import User
from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth import authenticate
from customers.models import customers

class movies(forms.Form):
	mname = forms.CharField(max_length=50)
	genre_choice=(('AC','Action'),
					('TH','Thriller'),
					('RM','Romance'),
					('Co','Comedy'))
	genre = forms.ChoiceField(choices=genre_choice)
	year = forms.IntegerField()
	description = forms.CharField(max_length=500)
	price = forms.FloatField()
	fname=forms.ModelChoiceField(queryset=customers.objects,required=False)


	
