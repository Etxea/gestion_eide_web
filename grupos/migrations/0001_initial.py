# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumno'
        db.create_table(u'alumnos_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('apellido1', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('apellido2', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('telefono1', self.gf('django.db.models.fields.CharField')(default='', max_length=9)),
            ('telefono2', self.gf('django.db.models.fields.CharField')(default='', max_length=9)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, null=True, blank=True)),
            ('cuenta_bancaria', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('localidad', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('cp', self.gf('django.db.models.fields.CharField')(default='', max_length=5)),
            ('dni', self.gf('django.db.models.fields.CharField')(default='', max_length=9, null=True, blank=True)),
        ))
        db.send_create_signal(u'alumnos', ['Alumno'])


    def backwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table(u'alumnos_alumno')


    models = {
        u'alumnos.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellido1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'apellido2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'cp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'}),
            'cuenta_bancaria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'dni': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'telefono1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '9'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '9'})
        }
    }

    complete_apps = ['alumnos']