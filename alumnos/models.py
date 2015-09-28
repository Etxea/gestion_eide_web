# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from profesores.models import Profesor

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

class Ano(models.Model):
	nombre = models.CharField(max_length=25,default="")
	activo = models.BooleanField(default=False)

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

class Historia(models.Model):
	alumno = models.ForeignKey('Alumno')
	fecha = models.DateField(auto_now_add=True)
	tipo = models.CharField(max_length=25,default="")
	anotacion = models.CharField(max_length=25,default="")

class Aula(models.Model):
    ##nombre = models.CharField()
    numero = models.DecimalField(max_digits=3,decimal_places=0)
    piso = models.CharField(max_length=25,default="")
    aforo = models.DecimalField(max_digits=3,decimal_places=0,default=14)

#~ class Clase(models.Model):
    #~ dia_semana = models.CharField(max_length=15,default="")
    #~ aula = models.ForeignKey('Aula')
    #~ horario = models.CharField(max_length=25,default="")
    #~ profesor = models.ManyToManyField('Profesor')
    #~ grupo = models.ManyToManyField('Grupo')

class Curso(models.Model):
    nombre = models.CharField(max_length=25,default="")
    precio = models.FloatField(default=100)
    ##No obligatorios
    examen = models.CharField(max_length=25,default="")
    nivel = models.CharField(max_length=25,default="")
    libros = models.ManyToManyField('Libro')
    nota_aprobado = models.FloatField(default=50)
    solo_examen_final = models.BooleanField(default=False)

class Grupo(models.Model):
    nombre = models.CharField(max_length=25,default="")
    curso = models.ForeignKey('Curso')    
    num_max = models.DecimalField(max_digits=2,decimal_places=0,default=14) #El tamano default no es lo mejor que este aqui, pero bueno
    menores = models.BooleanField(default=False)

class Festivo(models.Model):
    ano = models.DecimalField(max_digits=4,decimal_places=0)
    mes = models.DecimalField(max_digits=2,decimal_places=0)
    dia = models.DecimalField(max_digits=2,decimal_places=0)
    inicio = models.BooleanField(default=False)
    fin = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=250,default="",blank=True,null=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=25,default="")
    autor = models.CharField(max_length=25,default="")
    isbn = models.CharField(max_length=25,default="")
    editorial = models.CharField(max_length=25,default="")
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
