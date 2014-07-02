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

DURACION = (
    (15, _('1/4 hora')),
    (30, _('1/2 hora')),
    (45, _('3/4 hora')),
    (55, _('55min')),
    (60, _('1h')),
    (90, _('1h y 1/2')),
    (120, _('2h')),
    (150, _('2h y 1/2')),
    (180, _('3h')),
    (210, _('3h y 1/2')),
    (240, _('4h')),
    (270, _('4h y 1/2'))
    
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
    duracion = models.DecimalField(decimal_places=0,max_digits=3, choices= DURACION,default=60)
    profesor = models.ForeignKey(Profesor)
    def get_absolute_url(self):
        return reverse_lazy("curso_detalle",args=(self.curso.id,))

## Para el calendario
from calendar import HTMLCalendar
from datetime import date
## sacado de http://uggedal.com/journal/creating-a-flexible-monthly-calendar-in-django/
class ClasesCalendar(HTMLCalendar):

    def __init__(self, workouts):
        super(ClasesCalendar, self).__init__()
        self.workouts = workouts
        print self.workouts

    def formatday(self, day, weekday):
        print "somos format day"
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            print "Mirando si",day,"esta en ",self.workouts
            if day in self.workouts:
                cssclass += ' filled'
                body = []
                #body = ['<div>']
                #body.append("clase")
                #body.append("</div>")
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(ClasesCalendar, self).formatmonth(year, month)


    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)


