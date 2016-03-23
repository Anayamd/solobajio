from django.contrib import admin
from .models import Owner, Package, Industry, Negocio, NegocioImg, OpeningHour

class HoursInline(admin.TabularInline):
	model = OpeningHour
	extra = 5
	max_num = 7

class ImageInline(admin.StackedInline):
	model = NegocioImg

class NegocioAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'package', 'industry', 'published_date', 'ranking')
	search_fields = ('name',)
	list_filter = ('published_date', 'industry__ind_type', 'package__cost',)
	inlines = [ HoursInline, ImageInline, ]

class ImgAdmin(admin.ModelAdmin):
	list_display = ('negocio', 'admin_thumbnail')
	list_filter = ('negocio__name',)

class IndustryAdmin(admin.ModelAdmin):
	list_display = ('ind_type', 'icon')
	list_display = ('ind_type', 'admin_thumbnail')

admin.site.register(Owner)
admin.site.register(Package)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Negocio, NegocioAdmin)
admin.site.register(NegocioImg, ImgAdmin)