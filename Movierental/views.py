from django.shortcuts import render,redirect
from django.http import HttpResponse
from Movierental import urls
from customers.forms import customers as custform,loginform
from movies.forms import *
from customers.models import customers as cust
from movies.models import mmovies
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from mo import
from django.db.models import Q

from django.views.generic import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serialisers import MovieSerializer,CustomerSerializer
from Movierental.urls import *


def index(request):
	if request.method == 'POST':
		form = loginform(request.POST)
		if form.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]

			user = authenticate(request, username=username, password=password)
			print(username, password)
			if User.objects.filter(username=username).exists():
				login(request, user)
				return redirect("addcust")
			else:
				return render(request, 'index.html', {"form":form})

	else:
		form = loginform()
	return render(request, 'index.html', {"form":form})  
	
def logout_view(request):
    logout(request)
    return render(request, 'index.html')

@login_required(login_url='index')
def homepage(request):
	return render(request, 'homepage.html')


@login_required(login_url='index')
def addcust(request):
	if request.method == 'POST':
		form1= custform(request.POST)
		print(form1)
		if form1.is_valid():
			fname = form1.cleaned_data["fname"]
			lname = form1.cleaned_data["lname"]
			birthdate = form1.cleaned_data["birthdate"]
			pnumber = form1.cleaned_data["pnumber"]
			address= form1.cleaned_data["address"]
			cust_info = cust(fname=fname,lname=lname,birthdate=birthdate,pnumber=pnumber,address=address)
			cust_info.save()
			return redirect('searchcust')
	else:
		# when there is a get request
		# or you are trying to see the form on the page
		print("You made a GET request")
		form1 = custform()
	return render(request, 'addcustomers.html',{"form":form1})



@login_required(login_url='index')
def addmovies(request):
	if request.method == 'POST':
		form= movies(request.POST)
		print(form)
		if form.is_valid():
			mname = form.cleaned_data["mname"]
			genre = form.cleaned_data["genre"]
			year = form.cleaned_data["year"]
			description = form.cleaned_data["description"]
			price= form.cleaned_data["price"]
			fname=form.cleaned_data["fname"]
			mov_info =movies(mname=mname,genre=genre,year=year,description=description,price=price,fname=fname)
			mov_info.save()
			return redirect('listofmovies')
	else:
		# when there is a get request
		# either you are trying to see the page
		# or you are trying to see the form on the page
		print("You made a GET request")
		form = movies()
	
	return render(request, 'addmovies.html',{"form":form})




@login_required(login_url='index')
def listofcustomers(request):

	all_cust = cust.objects.all()
	
	return render(request, 'listofcustomers.html',{"customers": all_cust})



@login_required(login_url='index')
def listofmovies(request):
	all_movies = mmovies.objects.all()

	return render(request, 'listofmovies.html',{"movies": all_movies})





@login_required(login_url='index')
def searchmovies(request):
	return render(request, 'searchmovies.html')

@login_required(login_url='index')
def availablemovies(request):
	return render(request, 'availablemovies.html')




def delcust(request,id):
	
	instance = cust.objects.get(id=id)
	instance.delete()
	
	return redirect('searchcust')

def delmovie(request,id):
	instance = mmovies.objects.get(id=id)
	instance.delete()

	return redirect('listofmovies')


def updatecust(request,id=None):

	if request.method=="GET":

		instance = cust.objects.get(id=id)
		print("--------------", instance)
		form= custform(initial={"fname":instance.fname,"lname":instance.lname,"birthdate":instance.birthdate,"pnumber":instance.pnumber,"address":instance.address})
		print(form)
		#addcust(request)
		#return redirect('listofcustomers')
	elif request.method=="POST":
		print("hello worldllll")
		form=custform(request.POST)	
		
		if form.is_valid():
			print("I am inside here")
			fname = form.cleaned_data["fname"]
			lname = form.cleaned_data["lname"]
			birthdate = form.cleaned_data["birthdate"]
			pnumber = form.cleaned_data["pnumber"]
			address= form.cleaned_data["address"]
			instance = cust.objects.get(id=id)
			instance.fname=fname
			instance.lname=lname
			instance.birthdate=birthdate
			instance.pnumber=pnumber
			instance.address=address
			print(fname,lname)
			instance.save()
			return redirect('searchcust')
	

	

	
	return render(request, 'updatecust.html',{"customers":form})
	

@login_required(login_url='index')
def searchcust(request):

	query = request.GET.get('q', '')
	results = cust.objects.filter(Q(fname__icontains=query)  |  Q(lname__icontains=query) )

	return render(request,'searchcustomers.html', {'results': results})


@login_required(login_url='index')
def assignmovies(request):
	listmovie =mmovies.objects.filter(fname=None)

	listcust =cust.objects.all()
	
	if request.method=="POST":

		mid=request.POST['movieid']
		cid=request.POST['customerid']
		m = mmovies.objects.get(id=mid)
		c = cust.objects.get(id=cid)
		m.fname = c
		m.save()

		return redirect('availablemovies')
	return render(request, 'assignmovies.html',{"movies": listmovie, "customers": listcust})




@login_required(login_url='index')
def availablemovies(request):
	all_movies = mmovies.objects.filter(fname=None)
	return render(request, 'availablemovies.html',{"movies": all_movies})


def assignm(request,mid,cid):

        m = mmovies.objects.get(id=request.POST['mid'])
        c = cust.objects.get(id=request.POST['cid'])
        m.fname = m
        m.save()
        
        return redirect("searchcust")

class MovieList(APIView):

    def get(self,request):
        movie=mmovies.objects.all()
        serializer=MovieSerializer(movie, many=True)
        return Response(serializer.data)

class CustomerList(APIView):                                                   

    def get(self,request):
        customer=cust.objects.all()  
        serializer=CustomerSerializer(customer,many=True)
        return Response(serializer.data)

class CustList(APIView):

    def get(self,request,id):
        customer=cust.objects.filter(id=id)  
        serializer=CustomerSerializer(customer,many=True)
        return Response(serializer.data)

class MoList(APIView):

    def get(self,request,id):
        movie=
        .objects.filter(id=id) 
        serializer=MovieSerializer(movie, many=True)
        return Response(serializer.data)