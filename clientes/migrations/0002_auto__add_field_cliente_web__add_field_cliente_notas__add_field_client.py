# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cliente.web'
        db.add_column(u'clientes_cliente', 'web',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.notas'
        db.add_column(u'clientes_cliente', 'notas',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.contacto'
        db.add_column(u'clientes_cliente', 'contacto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='empresa', blank=True, to=orm['kontulari.Contacto']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cliente.web'
        db.delete_column(u'clientes_cliente', 'web')

        # Deleting field 'Cliente.notas'
        db.delete_column(u'clientes_cliente', 'notas')

        # Deleting field 'Cliente.contacto'
        db.delete_column(u'clientes_cliente', 'contacto_id')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'NIF': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'empresa'", 'blank': 'True', 'to': u"orm['kontulari.Contacto']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notas': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'kontulari.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'})
        }
    }

    complete_apps = ['clientes']