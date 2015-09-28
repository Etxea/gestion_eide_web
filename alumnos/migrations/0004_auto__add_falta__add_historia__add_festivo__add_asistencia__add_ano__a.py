# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Falta'
        db.create_table(u'alumnos_falta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('asistencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Asistencia'])),
            ('mes', self.gf('django.db.models.fields.DecimalField')(max_digits=1, decimal_places=0)),
            ('justificadas', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=3, decimal_places=0)),
            ('faltas', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=3, decimal_places=0)),
        ))
        db.send_create_signal(u'alumnos', ['Falta'])

        # Adding model 'Historia'
        db.create_table(u'alumnos_historia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Alumno'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('anotacion', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
        ))
        db.send_create_signal(u'alumnos', ['Historia'])

        # Adding model 'Festivo'
        db.create_table(u'alumnos_festivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ano', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=0)),
            ('mes', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('dia', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('inicio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observaciones', self.gf('django.db.models.fields.CharField')(default='', max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'alumnos', ['Festivo'])

        # Adding model 'Asistencia'
        db.create_table(u'alumnos_asistencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ano', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Ano'])),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Grupo'])),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Alumno'])),
            ('confirmado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('factura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('metalico', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('precio', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'alumnos', ['Asistencia'])

        # Adding model 'Ano'
        db.create_table(u'alumnos_ano', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'alumnos', ['Ano'])

        # Adding model 'Grupo'
        db.create_table(u'alumnos_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Curso'])),
            ('num_max', self.gf('django.db.models.fields.DecimalField')(default=14, max_digits=2, decimal_places=0)),
            ('menores', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'alumnos', ['Grupo'])

        # Adding model 'Aula'
        db.create_table(u'alumnos_aula', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=0)),
            ('piso', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('aforo', self.gf('django.db.models.fields.DecimalField')(default=14, max_digits=3, decimal_places=0)),
        ))
        db.send_create_signal(u'alumnos', ['Aula'])

        # Adding model 'Curso'
        db.create_table(u'alumnos_curso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('precio', self.gf('django.db.models.fields.FloatField')(default=100)),
            ('examen', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('nivel', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('nota_aprobado', self.gf('django.db.models.fields.FloatField')(default=50)),
            ('solo_examen_final', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'alumnos', ['Curso'])

        # Adding M2M table for field libros on 'Curso'
        m2m_table_name = db.shorten_name(u'alumnos_curso_libros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curso', models.ForeignKey(orm[u'alumnos.curso'], null=False)),
            ('libro', models.ForeignKey(orm[u'alumnos.libro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['curso_id', 'libro_id'])

        # Adding model 'Nota'
        db.create_table(u'alumnos_nota', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('asistencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumnos.Asistencia'])),
            ('trimestre', self.gf('django.db.models.fields.DecimalField')(max_digits=1, decimal_places=0)),
            ('grama', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0)),
            ('grama_baremo', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0)),
            ('expresion', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0)),
            ('expresion_baremo', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0)),
            ('lectura', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0)),
            ('lectura_baremo', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0)),
        ))
        db.send_create_signal(u'alumnos', ['Nota'])

        # Adding model 'Libro'
        db.create_table(u'alumnos_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('autor', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('isbn', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
            ('editorial', self.gf('django.db.models.fields.CharField')(default='', max_length=25)),
        ))
        db.send_create_signal(u'alumnos', ['Libro'])


    def backwards(self, orm):
        # Deleting model 'Falta'
        db.delete_table(u'alumnos_falta')

        # Deleting model 'Historia'
        db.delete_table(u'alumnos_historia')

        # Deleting model 'Festivo'
        db.delete_table(u'alumnos_festivo')

        # Deleting model 'Asistencia'
        db.delete_table(u'alumnos_asistencia')

        # Deleting model 'Ano'
        db.delete_table(u'alumnos_ano')

        # Deleting model 'Grupo'
        db.delete_table(u'alumnos_grupo')

        # Deleting model 'Aula'
        db.delete_table(u'alumnos_aula')

        # Deleting model 'Curso'
        db.delete_table(u'alumnos_curso')

        # Removing M2M table for field libros on 'Curso'
        db.delete_table(db.shorten_name(u'alumnos_curso_libros'))

        # Deleting model 'Nota'
        db.delete_table(u'alumnos_nota')

        # Deleting model 'Libro'
        db.delete_table(u'alumnos_libro')


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
            'examen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['alumnos.Libro']", 'symmetrical': 'False'}),
            'nivel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
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