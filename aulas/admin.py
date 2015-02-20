from django.contrib import admin
from models import *

class AulaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Aula, AulaAdmin)
