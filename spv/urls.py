from django.contrib import admin
from django.conf.urls import url
from . import views

admin.site.site_header = 'Solo Platform Variant'
admin.site.site_title = 'SPV'

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^lugares/$', views.lugares, name='lugares'),
	url(r'^lugares/(?P<filtro>.+)/$', views.lugares_search, name='lugares_search'),
	url(r'^eventos/$', views.eventos, name='eventos'),
	url(r'^info/(?P<pk>[0-9]+)/$', views.info, name='info'),
]