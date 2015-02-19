from models import *
from django.contrib import admin

class AlumnoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Alumno,AlumnoAdmin)