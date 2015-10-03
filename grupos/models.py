# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from cursos.models import Curso
from alumnos.models import *

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


class Grupo(models.Model):
    nombre = models.CharField(max_length=25,default="")
    curso = models.ForeignKey('Curso')    
    num_max = models.DecimalField(max_digits=2,decimal_places=0,default=14) #El tamano default no es lo mejor que este aqui, pero bueno
    menores = models.BooleanField(default=False)

class Asistencia(models.Model):
    ano = models.ForeignKey('Ano')
    grupo = models.ForeignKey('Grupo')
    alumno = models.ForeignKey('Alumno')
    confirmado = models.BooleanField(default=0)
    factura = models.BooleanField(default=0)
    metalico = models.BooleanField(default=0)
    precio = models.BooleanField(default="")
    #~ notas = MultipleJoin('Notas')
    #~ faltas = MultipleJoin('Notas')

class Nota(models.Model):
    asistencia = models.ForeignKey('Asistencia')
    trimestre = models.DecimalField(max_digits=1,decimal_places=0)
    grama = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    grama_baremo = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    expresion = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    expresion_baremo = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    lectura = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    lectura_baremo = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    
class Falta(models.Model):
    asistencia = models.ForeignKey('Asistencia')
    mes = models.DecimalField(max_digits=1,decimal_places=0)
    justificadas = models.DecimalField(max_digits=3,decimal_places=0,default="0")
    faltas = models.DecimalField(max_digits=3,decimal_places=0,default="0")

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
