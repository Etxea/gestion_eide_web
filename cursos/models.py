#  models.py
#
#  Copyright 2014 jon latorre <patataman@schrodinger>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from clientes.models import Cliente
from profesores.models import Profesor
import datetime


class Curso(models.Model):
    nombre = models.CharField(max_length=25,default="")
    precio = models.FloatField(default=100)
    ##No obligatorios
    examen = models.CharField(max_length=25,default="",blank=True,null=True)
    nivel = models.CharField(max_length=25,default="",blank=True,null=True)
    libros = models.ManyToManyField('Libro')
    nota_aprobado = models.FloatField(default=50)
    solo_examen_final = models.BooleanField(default=False)


#~ class CursoIntensivo(models.Model):
    #~ cliente = models.ForeignKey(Cliente)
    #~ nombre = models.CharField(max_length=100)
    #~ inicio = models.DateField(default=datetime.date.today())
    #~ fin = models.DateField(default=datetime.date.today())
    #~ def __unicode__(self):
        #~ return "%s - %s"%(self.cliente.nombre,self.nombre)
    #~ def get_absolute_url(self):
        #~ return reverse_lazy("curso_detalle",args=[self.id])

class Libro(models.Model):
    titulo = models.CharField(max_length=25,default="")
    autor = models.CharField(max_length=25,default="")
    isbn = models.CharField(max_length=25,default="")
    editorial = models.CharField(max_length=25,default="")

class Festivo(models.Model):
    ano = models.DecimalField(max_digits=4,decimal_places=0)
    mes = models.DecimalField(max_digits=2,decimal_places=0)
    dia = models.DecimalField(max_digits=2,decimal_places=0)
    inicio = models.BooleanField(default=False)
    fin = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=250,default="",blank=True,null=True)
