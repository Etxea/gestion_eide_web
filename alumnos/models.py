# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from profesores.models import Profesor
from grupos.models import *
from cursos.models import *


class Alumno(models.Model):
    nombre = models.CharField(max_length=25,default="")
    apellido1 = models.CharField(max_length=100,default="")
    apellido2 = models.CharField(max_length=100,default="",blank=True,null=True)
    telefono1 = models.CharField(max_length=9,default="")
    telefono2 = models.CharField(max_length=9,default="",blank=True,null=True)
    email = models.EmailField(default="",blank=True,null=True)
    cuenta_bancaria = models.CharField(max_length=25,default="")
    localidad = models.CharField(max_length=25,default="")
    cp = models.CharField(max_length=5,default="")
    dni = models.CharField(max_length=9,default="",blank=True,null=True)
    activo = models.BooleanField(default=True)
    #def __unicode__(self):
    #    return "%s %s (%s)"%(self.user.get_short_name(),self.user.last_name,self.user.username)

    def get_absolute_url(self):
        return "/alumnos/%s/"%self.id

class Historia(models.Model):
	alumno = models.ForeignKey('Alumno')
	fecha = models.DateField(auto_now_add=True)
	tipo = models.CharField(max_length=25,default="")
	anotacion = models.CharField(max_length=25,default="")
