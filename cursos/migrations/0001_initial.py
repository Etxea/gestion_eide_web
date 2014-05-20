# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Curso'
        db.create_table(u'cursos_curso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('inicio', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 20, 0, 0))),
            ('fin', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 20, 0, 0))),
        ))
        db.send_create_signal(u'cursos', ['Curso'])

        # Adding model 'Clase'
        db.create_table(u'cursos_clase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cursos.Curso'])),
            ('dia_semana', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=1, decimal_places=0)),
            ('hora', self.gf('django.db.models.fields.TimeField')()),
            ('duracion', self.gf('django.db.models.fields.TimeField')()),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profesores.Profesor'])),
        ))
        db.send_create_signal(u'cursos', ['Clase'])


    def backwards(self, orm):
        # Deleting model 'Curso'
        db.delete_table(u'cursos_curso')

        # Deleting model 'Clase'
        db.delete_table(u'cursos_clase')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'NIF': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cursos.clase': {
            'Meta': {'object_name': 'Clase'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cursos.Curso']"}),
            'dia_semana': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '1', 'decimal_places': '0'}),
            'duracion': ('django.db.models.fields.TimeField', [], {}),
            'hora': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profesores.Profesor']"})
        },
        u'cursos.curso': {
            'Meta': {'object_name': 'Curso'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 20, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 20, 0, 0)'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profesores.profesor': {
            'Meta': {'object_name': 'Profesor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['cursos']