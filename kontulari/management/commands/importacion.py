#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'patataman'
from django.core.management.base import BaseCommand, CommandError
from alumnos.models import Alumno as Alumno_new
from alumnos.models import Libro as Libro_new
from alumnos.models import Curso as Curso_new
from alumnos.models import Grupo as Grupo_new

from sqlobject import *
from sqlobject.inheritance import InheritableSQLObject

class Command(BaseCommand):
    args = 'sqlite database path'
    help = 'Importa datos de la BBDD de la anterior version del programa'

    def handle(self, *args, **options):
        if len(args)<1:
             raise CommandError('Falta fichero origen')
        else:
            bbdd = args[0]
            self.stdout.write('Iniciando importacion desde archivo %s'%bbdd)
            sqlhub.processConnection = connectionForURI('sqlite://'+bbdd)
            from alumnos.old_database_model import *

            self.stdout.write('Importamos los libros, primero vamos a vaciar la BBDD')
            Libro_new.objects.all().delete()
            busqueda = Libro.select()
            self.stdout.write('Encontrados %d libros'%busqueda.count())
            for libro in busqueda:
                l = Libro_new(\
                    titulo=libro.titulo,\
                    autor=libro.autor,\
                    isbn=libro.isbn,\
                    editorial=libro.editorial,\
                )
                l.save()
            
            self.stdout.write('Importamos los cursos, primero vamos a vaciar la BBDD')
            Curso_new.objects.all().delete()
            busqueda = Curso.select()
            self.stdout.write('Encontrados %d cursos'%busqueda.count())
            for curso in busqueda:
                c = Curso_new(\
					nombre = curso.nombre,\
					precio = curso.precio,\
					##No obligatorios
					examen = curso.examen,\
					nivel = curso.nivel,\
					nota_aprobado = curso.nota_aprobado,\
					solo_examen_final = curso.solo_examen_final,\
                )
                c.save()
                for libro in curso.libros:
					c.libros.add(Libro_new.objects.filter(isbn=libro.isbn)[0])
                
            self.stdout.write('Importamos los alumnos, primero vamos a vaciar la BBDD')
            Alumno_new.objects.all().delete()
            busqueda = Alumno.select()
            self.stdout.write('Encontrados %d alumnos'%busqueda.count())
            for persona in busqueda:
                #self.stdout.write('Anadiendo el alumno %d'%persona.id)
                try:
                    cuenta = "%d-%d-%d-%d"%(persona.banco.codigo,persona.sucursal,persona.dc,persona.cuenta)
                except:
                    cuenta = ""
                    self.stdout.write('Problema con la cuenta bancaria del alumno %d'%persona.id)
                a = Alumno_new(id=persona.id,\
                    activo = persona.activo,\
                    nombre = persona.nombre,\
                    apellido1 = persona.apellido1,\
                    apellido2 = persona.apellido2,\
                    telefono1 = persona.telefono1,\
                    telefono2 = persona.telefono2,\
                    email = persona.email,\
                    cuenta_bancaria = cuenta,\
                    localidad = persona.ciudad,\
                    cp = persona.cp,\
                    dni =persona.dni,)
                a.save()
                
            self.stdout.write('Importamos los grupos, primero vamos a vaciar la BBDD')
            Grupo_new.objects.all().delete()
            busqueda = Grupo.select()
            self.stdout.write('Encontrados %d grupos'%busqueda.count())
            for grupo in busqueda:
				g = Grupo_new(\
				
				)
