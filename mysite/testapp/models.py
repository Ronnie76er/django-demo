from django.db import models

class TestUser(models.Model):
	username = models.CharField(max_length = 200)
	create_date = models.DateTimeField('Date Created')

class UserInfo(models.Model):
	user = models.ForeignKey(TestUser)
	data_field1 = models.CharField(max_length=300)
	

# Create your models here.
