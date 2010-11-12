# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Maderable'
        db.create_table('indicador06_maderable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador06', ['Maderable'])

        # Adding model 'Forrajero'
        db.create_table('indicador06_forrajero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador06', ['Forrajero'])

        # Adding model 'Energetico'
        db.create_table('indicador06_energetico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador06', ['Energetico'])

        # Adding model 'Frutal'
        db.create_table('indicador06_frutal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador06', ['Frutal'])

        # Adding model 'ExistenciaArboles'
        db.create_table('indicador06_existenciaarboles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad_maderable', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_forrajero', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_energetico', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_frutal', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador06', ['ExistenciaArboles'])

        # Adding M2M table for field maderable on 'ExistenciaArboles'
        db.create_table('indicador06_existenciaarboles_maderable', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['indicador06.existenciaarboles'], null=False)),
            ('maderable', models.ForeignKey(orm['indicador06.maderable'], null=False))
        ))
        db.create_unique('indicador06_existenciaarboles_maderable', ['existenciaarboles_id', 'maderable_id'])

        # Adding M2M table for field forrajero on 'ExistenciaArboles'
        db.create_table('indicador06_existenciaarboles_forrajero', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['indicador06.existenciaarboles'], null=False)),
            ('forrajero', models.ForeignKey(orm['indicador06.forrajero'], null=False))
        ))
        db.create_unique('indicador06_existenciaarboles_forrajero', ['existenciaarboles_id', 'forrajero_id'])

        # Adding M2M table for field energetico on 'ExistenciaArboles'
        db.create_table('indicador06_existenciaarboles_energetico', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['indicador06.existenciaarboles'], null=False)),
            ('energetico', models.ForeignKey(orm['indicador06.energetico'], null=False))
        ))
        db.create_unique('indicador06_existenciaarboles_energetico', ['existenciaarboles_id', 'energetico_id'])

        # Adding M2M table for field frutal on 'ExistenciaArboles'
        db.create_table('indicador06_existenciaarboles_frutal', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('existenciaarboles', models.ForeignKey(orm['indicador06.existenciaarboles'], null=False)),
            ('frutal', models.ForeignKey(orm['indicador06.frutal'], null=False))
        ))
        db.create_unique('indicador06_existenciaarboles_frutal', ['existenciaarboles_id', 'frutal_id'])


    def backwards(self, orm):
        
        # Deleting model 'Maderable'
        db.delete_table('indicador06_maderable')

        # Deleting model 'Forrajero'
        db.delete_table('indicador06_forrajero')

        # Deleting model 'Energetico'
        db.delete_table('indicador06_energetico')

        # Deleting model 'Frutal'
        db.delete_table('indicador06_frutal')

        # Deleting model 'ExistenciaArboles'
        db.delete_table('indicador06_existenciaarboles')

        # Removing M2M table for field maderable on 'ExistenciaArboles'
        db.delete_table('indicador06_existenciaarboles_maderable')

        # Removing M2M table for field forrajero on 'ExistenciaArboles'
        db.delete_table('indicador06_existenciaarboles_forrajero')

        # Removing M2M table for field energetico on 'ExistenciaArboles'
        db.delete_table('indicador06_existenciaarboles_energetico')

        # Removing M2M table for field frutal on 'ExistenciaArboles'
        db.delete_table('indicador06_existenciaarboles_frutal')


    models = {
        'indicador06.energetico': {
            'Meta': {'object_name': 'Energetico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador06.existenciaarboles': {
            'Meta': {'object_name': 'ExistenciaArboles'},
            'cantidad_energetico': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_forrajero': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_frutal': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_maderable': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'energetico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador06.Energetico']", 'symmetrical': 'False'}),
            'forrajero': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador06.Forrajero']", 'symmetrical': 'False'}),
            'frutal': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador06.Frutal']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maderable': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador06.Maderable']", 'symmetrical': 'False'})
        },
        'indicador06.forrajero': {
            'Meta': {'object_name': 'Forrajero'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador06.frutal': {
            'Meta': {'object_name': 'Frutal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador06.maderable': {
            'Meta': {'object_name': 'Maderable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
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
        }
    }

    complete_apps = ['indicador06']
