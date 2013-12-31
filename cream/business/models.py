from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
	name = models.TextField()

class Area(models.Model):
	organization = models.ForeignKey(Organization)
	name = models.TextField()

class Person(models.Model):	
	company = models.ManyToManyField(Organization, null=True)
	user = models.ForeignKey(User, null=True)






class Skill(models.Model):
	organization = models.ForeignKey(Organization)
	name = models.TextField()

class PersonSkill(models.Model):
	person = models.ForeignKey(Person)
	skill = models.ForeignKey(Skill)
	level = models.IntegerField()



class Hierarchy(models.Model):
	person = models.ForeignKey(Person)
	manager = models.ForeignKey(Person)
	date_from = models.DateField(null=True, blank=True)
	date_to = models.DateField(null=True, blank=True)
	ending_reason = models.TextField()