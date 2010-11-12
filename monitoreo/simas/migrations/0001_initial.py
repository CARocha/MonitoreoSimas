# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Recolector'
        db.create_table('simas_recolector', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('simas', ['Recolector'])

        # Adding model 'Organizaciones'
        db.create_table('simas_organizaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('correo_electronico', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'], null=True, blank=True)),
            ('logo', self.gf('monitoreo.simas.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('sitio_web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('simas', ['Organizaciones'])

        # Adding model 'Encuesta'
        db.create_table('simas_encuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('recolector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Recolector'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('finca', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comunidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Comunidad'])),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Organizaciones'])),
        ))
        db.send_create_signal('simas', ['Encuesta'])

        # Adding model 'Tenencia'
        db.create_table('simas_tenencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parcela', self.gf('django.db.models.fields.IntegerField')()),
            ('solar', self.gf('django.db.models.fields.IntegerField')()),
            ('dueno', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('simas', ['Tenencia'])


    def backwards(self, orm):
        
        # Deleting model 'Recolector'
        db.delete_table('simas_recolector')

        # Deleting model 'Organizaciones'
        db.delete_table('simas_organizaciones')

        # Deleting model 'Encuesta'
        db.delete_table('simas_encuesta')

        # Deleting model 'Tenencia'
        db.delete_table('simas_tenencia')


    models = {
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'simas.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Organizaciones']"}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Recolector']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        'simas.organizaciones': {
            'Meta': {'object_name': 'Organizaciones'},
            'celular': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']", 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('monitoreo.simas.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'simas.recolector': {
            'Meta': {'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'simas.tenencia': {
            'Meta': {'object_name': 'Tenencia'},
            'dueno': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcela': ('django.db.models.fields.IntegerField', [], {}),
            'solar': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['simas']
