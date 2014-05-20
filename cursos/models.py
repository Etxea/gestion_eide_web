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

DIAS_SEMANA = (
    (1, _('Lunes')),
    (2, _('Martes')),
    (3, _('Miercoles')),
    (4, _('Jueves')),
    (5, _('Viernes'))
)


class Curso(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100)
    inicio = models.DateField(default=datetime.date.today())
    fin = models.DateField(default=datetime.date.today())
    def __unicode__(self):
        return "%s - %s"%(self.cliente.nombre,self.nombre)
    def get_absolute_url(self):
        return reverse_lazy("curso_detalle",args=[self.id])

class Clase(models.Model):
    curso = models.ForeignKey(Curso)
    dia_semana = models.DecimalField(decimal_places=0,max_digits=1,choices= DIAS_SEMANA,default=1)
    hora = models.TimeField()
    duracion = models.TimeField()
    profesor = models.ForeignKey(Profesor)
    def get_absolute_url(self):
        return reverse_lazy("curso_detalle",args=(self.curso.id,))


