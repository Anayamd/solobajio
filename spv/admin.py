from django.contrib import admin
from .models import Owner, Package, Industry, Negocio, NegocioImg

admin.site.register(Owner)
admin.site.register(Package)
admin.site.register(Industry)
admin.site.register(Negocio)
admin.site.register(NegocioImg)
