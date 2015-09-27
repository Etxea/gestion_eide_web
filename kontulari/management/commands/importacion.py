#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'patataman'
from django.core.management.base import BaseCommand, CommandError
from alumnos.models import Alumno as Alumno_new

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
            self.stdout.write('Vamos a vaciar la BBDD')
            Alumno_new.objects.all().delete()
            sqlhub.processConnection = connectionForURI('sqlite://'+bbdd)
            from alumnos.old_database_model import *
            busqueda = Alumno.select()
            self.stdout.write('Encontrados %d alumnos'%busqueda.count())
            for persona in busqueda:
                #self.stdout.write('Anadiendo el alumno %d'%persona.id)
                try:
                    cuenta = "%d%d%d%d"%(persona.banco.codigo,persona.sucursal,persona.dc,persona.cuenta)
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
