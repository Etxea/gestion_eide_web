from models import *
from django.contrib import admin

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente,ClienteAdmin)
