from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# https://django-taggit.readthedocs.org/en/latest/getting_started.html
from taggit.managers import TaggableManager

WEEKDAYS = [
	(1, "Monday"),
	(2, "Tuesday"),
	(3, "Wednesday"),
	(4, "Thursday"),
	(5, "Friday"),
	(6, "Saturday"),
	(7, "Sunday"),
]

class Owner(models.Model):
	holder = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.holder

class Package(models.Model):
	pkg_name = models.CharField(max_length=50)
	cost = models.SmallIntegerField()
	top = models.BooleanField()
	slider = models.BooleanField()
	mentions = models.SmallIntegerField()

	def __str__(self):
		return self.pkg_name

class Industry(models.Model):
	ind_type = models.CharField(max_length=50)
	icon = models.ImageField()

	def __str__(self):
		return self.ind_type

class Negocio(models.Model):
	owner = models.ForeignKey('spv.Owner', related_name='owner')
	package = models.ForeignKey('spv.Package', related_name='package')
	industry = models.ForeignKey('spv.Industry', related_name='industry')
	
	name = models.CharField(max_length=200)
	slogan = models.CharField(max_length=200, blank=True, null=True)
	info = models.TextField()
	email = models.EmailField(blank=True, null=True)
	location = models.TextField()

	cel1 = models.CharField(max_length=25, blank=True, null=True)
	cel2 = models.CharField(max_length=25, blank=True, null=True)
	cel3 = models.CharField(max_length=25, blank=True, null=True)
	social_fb = models.CharField(max_length=200, blank=True, null=True)
	social_twitter = models.CharField(max_length=200, blank=True, null=True)
	social_website = models.URLField(blank=True, null=True)
	
	tags = TaggableManager()
	published_date = models.DateTimeField(blank=True, null=True)
	fb_mentions = models.SmallIntegerField()

	def publicar(self):
		self.published_date = timezone.now()
		self.fb_mentions = self.package.mentions
		self.save()

	def __str__(self):
		return self.name

class OpeningHours(models.Model):
	store = models.ForeignKey('spv.Negocio', related_name='store')
	weekday = models.SmallIntegerField(choices=WEEKDAYS,unique=True)
	from_hour = models.TimeField()
	to_hour = models.TimeField()

class NegocioImg(models.Model):
	negocio = models.ForeignKey('spv.Negocio', related_name='negocio')
	image = models.ImageField()

	def __str__(self):
		return self.negocio.name