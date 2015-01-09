from django.db import models
from django.contrib import admin

class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=60)
	def __unicode__(self):
		return self.name


class Author(models.Model):
	first_name=models.CharField(max_length=30)
	middle_name=models.CharField(max_length=60)
	email=models.EmailField()
	def __unicode__(self):
		return u'%s %s'%(self.first_name,self.middle_name)

class Book(models.Model):
	title=models.CharField(max_length=30)
	authors=models.CharField(max_length=60)
	Publisher=models.ForeignKey(Publisher)
	Publisher_date=models.DateField()
	def __unicode__(self):
		return self.title
