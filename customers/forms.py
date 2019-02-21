from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate



class customers(forms.Form):
	fname = forms.CharField(max_length=50)
	lname = forms.CharField(max_length=60)
	birthdate = forms.DateField()
	pnumber = forms.CharField(max_length=15)
	address = forms.CharField(max_length=50)

class loginform(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())



	
