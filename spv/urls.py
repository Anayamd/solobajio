from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^mensaje/$', views.mensaje, name='mensaje'),
	url(r'^lugares/$', views.lugares, name='lugares'),
	url(r'^lugares/(?P<filtro>.+)/$', views.lugares, name='lugares'),
	url(r'^eventos/$', views.eventos, name='eventos'),
	url(r'^info/(?P<pk>[0-9]+)/$', views.info, name='info'),
	url(r'^contacto/$', views.contacto, name='contacto'),
]