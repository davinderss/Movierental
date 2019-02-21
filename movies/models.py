from django.db import models
from customers.models import customers

 
class mmovies(models.Model):
	mname = models.CharField(max_length=50)
	genre_choice=(('AC','Action'),
					('TH','Thriller'),
					('RM','Romance'),
					('Co','Comedy'))
	genre = models.CharField(max_length=60, choices=genre_choice)
	year = models.IntegerField()
	description = models.CharField(max_length=500)
	price = models.FloatField()
	fname=models.ForeignKey(customers, on_delete=models.SET_NULL,blank=True,null=True)

	def __str__(self):
		return self.mname