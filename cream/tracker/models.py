from django.db import models

from business.models import * 
from projects.models import *

class Activity(models.Model):
	user = models.ForeignKey(Person)
	project = models.ForeignKey(project)
	task = models.ForeignKey(Task)

	location = models.ForeignKey(Organization)

	class Meta:
		abstract=True

class PlannedActivity(Activity):
	planned_start = models.DateTimeField()
	planned_end = models.DateTimeField()

class ReportedActivity(Activity):
	planned = models.ForeignKey(PlannedActivity, null=True)
	time_start = models.DateTimeField()
	time_end = models.DateTimeField()

	description = models.TextField()
	
