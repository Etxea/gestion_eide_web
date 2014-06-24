# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClienteContacto'
        db.create_table(u'clientes_clientecontacto', (
            (u'contacto_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kontulari.Contacto'], unique=True, primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
        ))
        db.send_create_signal(u'clientes', ['ClienteContacto'])

        # Deleting field 'Cliente.contacto'
        db.delete_column(u'clientes_cliente', 'contacto_id')


    def backwards(self, orm):
        # Deleting model 'ClienteContacto'
        db.delete_table(u'clientes_clientecontacto')

        # Adding field 'Cliente.contacto'
        db.add_column(u'clientes_cliente', 'contacto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='empresa', to=orm['kontulari.Contacto'], blank=True),
                      keep_default=False)


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'NIF': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notas': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'clientes.clientecontacto': {
            'Meta': {'object_name': 'ClienteContacto', '_ormbases': [u'kontulari.Contacto']},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            u'contacto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kontulari.Contacto']", 'unique': 'True', 'primary_key': 'True'})
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