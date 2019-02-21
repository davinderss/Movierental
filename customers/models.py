from django.db import models



 
class customers(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=60)
	birthdate = models.DateField()
	pnumber = models.CharField(max_length=15)
	address = models.TextField(max_length=50)

	def __str__(self):
		return self.fname + " "+ self.lname

class index(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.username
