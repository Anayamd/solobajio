from django.contrib import admin
from django.conf.urls import url
from . import views

admin.site.site_header = 'Solo Platform Admin'

urlpatterns = [
	url(r'^$', views.home, name='home'),
]