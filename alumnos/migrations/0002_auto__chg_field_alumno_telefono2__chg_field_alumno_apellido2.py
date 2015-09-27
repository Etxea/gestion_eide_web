# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Alumno.telefono2'
        db.alter_column(u'alumnos_alumno', 'telefono2', self.gf('django.db.models.fields.CharField')(max_length=9, null=True))

        # Changing field 'Alumno.apellido2'
        db.alter_column(u'alumnos_alumno', 'apellido2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Alumno.telefono2'
        db.alter_column(u'alumnos_alumno', 'telefono2', self.gf('django.db.models.fields.CharField')(max_length=9))

        # Changing field 'Alumno.apellido2'
        db.alter_column(u'alumnos_alumno', 'apellido2', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'alumnos.alumno': {
            'Meta': {'object_name': 'Alumno'},
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
        }
    }

    complete_apps = ['alumnos']