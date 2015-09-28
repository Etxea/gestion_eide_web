# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Curso.nivel'
        db.alter_column(u'alumnos_curso', 'nivel', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'Curso.examen'
        db.alter_column(u'alumnos_curso', 'examen', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

    def backwards(self, orm):

        # Changing field 'Curso.nivel'
        db.alter_column(u'alumnos_curso', 'nivel', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'Curso.examen'
        db.alter_column(u'alumnos_curso', 'examen', self.gf('django.db.models.fields.CharField')(max_length=25))

    models = {
        u'alumnos.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'apellido1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'apellido2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'}),
            'cuenta_bancaria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'dni': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'telefono1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '9'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        u'alumnos.ano': {
            'Meta': {'object_name': 'Ano'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'})
        },
        u'alumnos.asistencia': {
            'Meta': {'object_name': 'Asistencia'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Alumno']"}),
            'ano': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Ano']"}),
            'confirmado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'factura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metalico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'precio': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'alumnos.aula': {
            'Meta': {'object_name': 'Aula'},
            'aforo': ('django.db.models.fields.DecimalField', [], {'default': '14', 'max_digits': '3', 'decimal_places': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '0'}),
            'piso': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'})
        },
        u'alumnos.curso': {
            'Meta': {'object_name': 'Curso'},
            'examen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['alumnos.Libro']", 'symmetrical': 'False'}),
            'nivel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'nota_aprobado': ('django.db.models.fields.FloatField', [], {'default': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {'default': '100'}),
            'solo_examen_final': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'alumnos.falta': {
            'Meta': {'object_name': 'Falta'},
            'asistencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Asistencia']"}),
            'faltas': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '3', 'decimal_places': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'justificadas': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '3', 'decimal_places': '0'}),
            'mes': ('django.db.models.fields.DecimalField', [], {'max_digits': '1', 'decimal_places': '0'})
        },
        u'alumnos.festivo': {
            'Meta': {'object_name': 'Festivo'},
            'ano': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '0'}),
            'dia': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'fin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mes': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'observaciones': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'alumnos.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Curso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'num_max': ('django.db.models.fields.DecimalField', [], {'default': '14', 'max_digits': '2', 'decimal_places': '0'})
        },
        u'alumnos.historia': {
            'Meta': {'object_name': 'Historia'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Alumno']"}),
            'anotacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'})
        },
        u'alumnos.libro': {
            'Meta': {'object_name': 'Libro'},
            'autor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'editorial': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'})
        },
        u'alumnos.nota': {
            'Meta': {'object_name': 'Nota'},
            'asistencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['alumnos.Asistencia']"}),
            'expresion': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0'}),
            'expresion_baremo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0'}),
            'grama': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0'}),
            'grama_baremo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lectura': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0'}),
            'lectura_baremo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0'}),
            'trimestre': ('django.db.models.fields.DecimalField', [], {'max_digits': '1', 'decimal_places': '0'})
        }
    }

    complete_apps = ['alumnos']