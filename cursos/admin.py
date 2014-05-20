from django.contrib import admin
from models import *

class CursoAdmin(admin.ModelAdmin):
    pass

class ClaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Clase,ClaseAdmin)
admin.site.register(Curso,CursoAdmin)
