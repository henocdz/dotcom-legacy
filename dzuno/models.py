from django.db import models

# Create your models here.

class Me(models.Model):
	name = models.CharField(max_length=140, null=False)
	bio_es = models.TextField()
	bio_en = models.TextField(null=True,blank=True)
	pic = models.ImageField(upload_to="usr")

class Course(models.Model):
	name = models.CharField(max_length=80,null=False)
	thumbnail = models.ImageField(upload_to="courses/")
	playlist_id = models.CharField(max_length=11)
	date = models.DateTimeField(auto_now_add=True)

class Tutorial(models.Model):
	yt_id = models.CharField(max_length=11,primary_key=True)
	name = models.CharField(max_length = 80)
	thumbnail = models.ImageField(upload_to="tutorials/")
	date = models.DateTimeField()
	duration = models.BigIntegerField()
	course = models.ForeignKey('Course',null=True,blank=True)

class Project(models.Model):
	name = models.CharField(max_length=80)
	site_url = models.URLField()
	description = models.TextField()
	thumbnail = models.ImageField(upload_to="projects/")
	languages = models.TextField()
	taip = models.SmallIntegerField()
	date_a = models.DateTimeField(auto_now_add=True)
	date = models.DateTimeField()

#class Friend(models.Model):
	#pass