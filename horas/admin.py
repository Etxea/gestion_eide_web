from models import *
from django.contrib import admin

class ParteAdmin(admin.ModelAdmin):
    pass
class BonoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bono,BonoAdmin)
admin.site.register(Parte,ParteAdmin)