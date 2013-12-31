from django.db import models

from business.models import *


class Project(models.Model):
	name = models.TextField()
	is_support = models.BooleanField()

class ProjectTeamMember(models.Model):
	project = models.ForeignKey(Project)
	organization = models.ForeignKey(Organization)
	member = models.ForeignKey(Person)

class ProjectManager(models.Model):
	member = models.ForeignKey(ProjectTeamMember, unique=True, related_name="manager")
	date_from = models.DateField(null=True, blank=True)
	date_to = models.DateField(null=True, blank=True)


class Task(models.Model):
	project = models.ForeignKey(Project)
	name = models.TextField()
	follows = models.ManyToManyField('Task', null=True, blank=True, related_name="precedes")

class TaskPlan(models.Model):
	task = models.ForeignKey(Task)
	planned_start = models.DateTimeField()
	planned_end = models.DateTimeField()

class TaskStart(models.Model):
	task = models.ForeignKey(Task, unique=True)
	time = models.DateTimeField(auto_now=True)

class TaskEnd(models.Model):
	task = models.ForeignKey(Task, unique=True)
	time = models.DateTimeField(auto_now=True)

class ProjectStart(models.Model):
	task = models.ForeignKey(Project, unique=True)
	time = models.DateTimeField(auto_now=True)

class ProjectEnd(models.Model):
	task = models.ForeignKey(Project, unique=True)
	time = models.DateTimeField(auto_now=True)
