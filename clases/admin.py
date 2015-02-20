from django.contrib import admin
from models import *

class ClaseAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Clase, ClaseAdmin)


