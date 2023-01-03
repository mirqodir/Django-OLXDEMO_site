from django.db import models

class Menu(models.Model):
	nomi = models.CharField(max_length=250)
	malumot = models.TextField()
	narxi = models.CharField(max_length=10)
	image = models.ImageField(upload_to="images/")



	def __str__(self):
		return self.nomi




