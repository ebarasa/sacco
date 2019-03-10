from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	name = models.CharField()
	def __str__(self):
		return f'{self.user.username} Profile'

class Matatu(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField()
	name=models.CharField()

class Activities(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


class Report(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)