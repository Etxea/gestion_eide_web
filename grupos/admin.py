from models import *
from django.contrib import admin

class GrupoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Grupo,GrupoAdmin)
