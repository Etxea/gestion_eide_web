from django.db import models
from django.contrib.auth.models import User


class Alumno(models.Model):
    nombre = models.CharField(max_length=25,default="")
    apellido1 = models.CharField(max_length=100,default="")
    apellido2 = models.CharField(max_length=100,default="")
    telefono1 = models.CharField(max_length=9,default="")
    telefono2 = models.CharField(max_length=9,default="")
    email = models.EmailField()
    cuenta_bancaria = models.CharField(max_length=25,default="")
    localidad = models.CharField(max_length=25,default="")
    cp = models.CharField(max_length=5,default="")
    dni = models.CharField(max_length=9,default="")
    #def __unicode__(self):
    #    return "%s %s (%s)"%(self.user.get_short_name(),self.user.last_name,self.user.username)

    def get_absolute_url(self):
        return "/alumno/%s/"%self.id