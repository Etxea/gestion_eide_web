from models import *
from django.contrib import admin

class AsistenciaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Asistencia,AsistenciaAdmin)
