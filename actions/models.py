from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
	gender_option = [('Male', 'Male'), ('Female', 'Female')]
	name = models.CharField(max_length=30)
	dob = models.DateField()
	gender = models.CharField(max_length=10, choices=gender_option)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		 	return reverse("personal_view", kwargs={"member_id": self.id})


class Work(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	description	= models.TextField()
	due = models.DateField(default=date.today())

class Action(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description	= models.TextField()
	due = models.DateField(default=date.today())
	finish = models.BooleanField(default=False)

