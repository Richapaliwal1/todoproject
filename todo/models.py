from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS_CHOICE = (
	("OPEN", "OPEN"),
	("WORKING", "WORKING"),
	("DONE", "DONE"),
	("OVERDUE", "OVERDUE"),
)

class Tags(models.Model):
	tag = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.tag

class Todolist(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	tag = models.ManyToManyField(Tags)
	status = models.CharField(max_length=10, choices = STATUS_CHOICE, default = "OPEN")
	due_date = models.DateTimeField(auto_now=True,auto_now_add=False, null=True, )
	timestamp = models.DateTimeField(auto_now_add=True,editable=False)
	updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title