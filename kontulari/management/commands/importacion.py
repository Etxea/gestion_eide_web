# -*- coding: utf-8 -*-
__author__ = 'patataman'
from django.core.management.base import BaseCommand, CommandError
from alumnos.models import Alumno

class Command(BaseCommand):
    args = 'sqlite database path'
    help = 'Importa datos de la BBDD de la anterior version del programa'

    def handle(self, *args, **options):
        if len(args)<1:
             raise CommandError('Falta fichero origen')
        else:
            bbdd = args[0]
            self.stdout.write('Iniciando importacion desde archivo %s'%bbdd)