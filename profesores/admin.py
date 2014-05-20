from models import *
from django.contrib import admin

class ProfesorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profesor,ProfesorAdmin)
