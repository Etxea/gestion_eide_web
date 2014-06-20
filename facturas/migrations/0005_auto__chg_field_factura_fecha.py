# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Factura.fecha'
        db.alter_column(u'facturas_factura', 'fecha', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Factura.fecha'
        db.alter_column(u'facturas_factura', 'fecha', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

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
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'empresa'", 'blank': 'True', 'to': u"orm['kontulari.Contacto']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notas': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'facturas.concepto': {
            'Meta': {'object_name': 'Concepto'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '3', 'decimal_places': '0'}),
            'descuento': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'}),
            'factura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturas.Factura']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'facturas.factura': {
            'Meta': {'object_name': 'Factura'},
            'borrador': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'descuento': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'forma_pago': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '2', 'decimal_places': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'pagada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'retencion': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0'}),
            'subtotal': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'kontulari.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'})
        }
    }

    complete_apps = ['facturas']