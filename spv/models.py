from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings

# https://django-taggit.readthedocs.org/en/latest/getting_started.html
from taggit.managers import TaggableManager

WEEKDAYS = [
	(1, "Lunes"),
	(2, "Martes"),
	(3, "Miércoles"),
	(4, "Jueves"),
	(5, "Viernes"),
	(6, "Sábado"),
	(7, "Domingo"),
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
	icon = models.ImageField(upload_to='img/industry/')

	def admin_thumbnail(self):
		return u'<img src="%s" style="max-height:30px;">' % (self.icon.url)
	admin_thumbnail.short_description = 'Thumbnail'
	admin_thumbnail.allow_tags = True

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
	visits = models.IntegerField(default=0)
	ranking = models.FloatField(default=0)

	def publicar(self):
		self.published_date = timezone.now()
		self.fb_mentions = self.package.mentions
		self.save()

	def __str__(self):
		return self.name

class OpeningHour(models.Model):
	store = models.ForeignKey('spv.Negocio', related_name='store')
	weekday = models.SmallIntegerField(choices=WEEKDAYS,unique=True)
	from_hour = models.TimeField()
	to_hour = models.TimeField()

class NegocioImg(models.Model):
	negocio = models.ForeignKey('spv.Negocio', related_name='images')

	def generate_folder_for_business(self, filename):
		# img/nombre_negocio/foto.jpg
		return 'img/' + self.negocio.name + '/' + filename

	image = models.ImageField(upload_to=generate_folder_for_business)

	def admin_thumbnail(self):
		return u'<img src="%s" style="max-height:30px;">' % (self.image.url)
	admin_thumbnail.short_description = 'Thumbnail'
	admin_thumbnail.allow_tags = True

	def __str__(self):
		return self.negocio.name

class Evento(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField()
	place = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		return self.title

class EventoImg(models.Model):
	evento = models.ForeignKey('spv.Evento', related_name='image')

	def generate_file_path(self, filename):
		# img/nombre_negocio/foto.jpg
		return 'img/eventos/' + filename

	image = models.ImageField(upload_to=generate_file_path)

	def admin_thumbnail(self):
		return u'<img src="%s" style="max-height:30px;">' % (self.image.url)
	admin_thumbnail.short_description = 'Thumbnail'
	admin_thumbnail.allow_tags = True

	def __str__(self):
		return self.evento.title