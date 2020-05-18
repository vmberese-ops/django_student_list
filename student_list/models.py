from django.db import models
from django.utils import timezone

class List(models.Model):
	lastname = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	yearlevel = models.CharField(max_length=200)
	course = models.CharField(max_length=200)
	gender = models.CharField(max_length=200)
	date = models.DateField(default=timezone.now)
	
	def __str__(self):
		return self.lastname + ", " + self.firstname