from django.contrib import admin
from .models import Owner, Package, Industry, Negocio, NegocioImg

class ImageInline(admin.StackedInline):
	model = NegocioImg

class NegocioAdmin(admin.ModelAdmin):
	list_display = ('owner', 'name', 'package', 'industry', 'published_date')
	search_fields = ('owner__holder', 'name')
	list_filter = ('published_date', 'industry__ind_type',)
	inlines = [ ImageInline, ]

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