from models import *
from django.contrib import admin

class FacturaAdmin(admin.ModelAdmin):
    pass

class ConceptoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Factura,FacturaAdmin)
admin.site.register(Concepto,ConceptoAdmin)
