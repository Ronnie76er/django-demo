from django.db import models

class TestUser(models.Model):
	username = models.CharField(max_length = 200)
	create_date = models.DateTimeField('Date Created')

	def __unicode__(self):
		return self.username

class UserInfo(models.Model):

	class Meta:
		permissions = (
			('view_user_info', "Can view the users info"),
		)


	user = models.ForeignKey(TestUser)
	data_field1 = models.CharField(max_length=300)

