from django.contrib import admin
from django.conf.urls import url
from . import views

admin.site.site_header = 'Solo Platform Variant'
admin.site.site_title = 'SPV'

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^lugares/$', views.lugares, name='lugares'),
	url(r'^eventos/$', views.eventos, name='eventos'),
]