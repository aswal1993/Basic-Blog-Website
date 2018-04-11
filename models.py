from django.db import models
from django import forms
from tinymce import models as tinymce_models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


# Create your models here.

class Data(models.Model):
	null=True
	first_name = models.CharField(max_length=30,blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	satus = models.CharField(max_length=300,null=True,blank=True)
	comments = models.CharField(max_length=3000,null=True,blank=True)
	search_fields = ('first_name','last_name','satus','comments')
	def __str__(self,first_name,last_name,satus,comments):
        
		self.first_name=first_name
		self.last_name=last_name
		self.satus=satus
		self.comments=comments

		return self.first_name,self.last_name,self.satus,self.comments

class data2(models.Model):
	post = models.CharField(max_length=200)
	description = tinymce_models.HTMLField()

class data3(models.Model):
	description=models.CharField(max_length=200)
	status=models.CharField(max_length=200)


class BlogModel(models.Model):
	name = models.CharField(max_length=30)
	blog = tinymce_models.HTMLField()
	image = models.ImageField(upload_to = 'myapp.templates/', default = 'pic_folder/None/no-img.jpg')
	slug = models.SlugField(unique=True, blank=True)
	#comment = tinymce_models.HTMLField()
	def save(self):
		self.slug = slugify(self.name)
		return super(BlogModel,self).save()

class CommentModel(models.Model):
	
	comment = tinymce_models.HTMLField()
	comment_F = models.ForeignKey(BlogModel,null=True)
	name = models.CharField(max_length=30,null=True)
	email = models.CharField(max_length=30,null=True)
	
	def save(self):
		return super(CommentModel,self).save()
		

class Publisher(models.Model):
	name = models.CharField(max_length=30)