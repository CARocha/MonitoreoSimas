# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Textura'
        db.create_table('indicador12_textura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Textura'])

        # Adding model 'Profundidad'
        db.create_table('indicador12_profundidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Profundidad'])

        # Adding model 'Densidad'
        db.create_table('indicador12_densidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Densidad'])

        # Adding model 'Pendiente'
        db.create_table('indicador12_pendiente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Pendiente'])

        # Adding model 'Drenaje'
        db.create_table('indicador12_drenaje', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Drenaje'])

        # Adding model 'Suelo'
        db.create_table('indicador12_suelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador12', ['Suelo'])

        # Adding M2M table for field textura on 'Suelo'
        db.create_table('indicador12_suelo_textura', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('textura', models.ForeignKey(orm['indicador12.textura'], null=False))
        ))
        db.create_unique('indicador12_suelo_textura', ['suelo_id', 'textura_id'])

        # Adding M2M table for field profundidad on 'Suelo'
        db.create_table('indicador12_suelo_profundidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('profundidad', models.ForeignKey(orm['indicador12.profundidad'], null=False))
        ))
        db.create_unique('indicador12_suelo_profundidad', ['suelo_id', 'profundidad_id'])

        # Adding M2M table for field lombrices on 'Suelo'
        db.create_table('indicador12_suelo_lombrices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['indicador12.densidad'], null=False))
        ))
        db.create_unique('indicador12_suelo_lombrices', ['suelo_id', 'densidad_id'])

        # Adding M2M table for field densidad on 'Suelo'
        db.create_table('indicador12_suelo_densidad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['indicador12.densidad'], null=False))
        ))
        db.create_unique('indicador12_suelo_densidad', ['suelo_id', 'densidad_id'])

        # Adding M2M table for field pendiente on 'Suelo'
        db.create_table('indicador12_suelo_pendiente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('pendiente', models.ForeignKey(orm['indicador12.pendiente'], null=False))
        ))
        db.create_unique('indicador12_suelo_pendiente', ['suelo_id', 'pendiente_id'])

        # Adding M2M table for field drenaje on 'Suelo'
        db.create_table('indicador12_suelo_drenaje', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('drenaje', models.ForeignKey(orm['indicador12.drenaje'], null=False))
        ))
        db.create_unique('indicador12_suelo_drenaje', ['suelo_id', 'drenaje_id'])

        # Adding M2M table for field materia on 'Suelo'
        db.create_table('indicador12_suelo_materia', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('suelo', models.ForeignKey(orm['indicador12.suelo'], null=False)),
            ('densidad', models.ForeignKey(orm['indicador12.densidad'], null=False))
        ))
        db.create_unique('indicador12_suelo_materia', ['suelo_id', 'densidad_id'])

        # Adding model 'Preparar'
        db.create_table('indicador12_preparar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Preparar'])

        # Adding model 'Traccion'
        db.create_table('indicador12_traccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Traccion'])

        # Adding model 'Fertilizacion'
        db.create_table('indicador12_fertilizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Fertilizacion'])

        # Adding model 'Conservacion'
        db.create_table('indicador12_conservacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador12', ['Conservacion'])

        # Adding model 'ManejoSuelo'
        db.create_table('indicador12_manejosuelo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analisis', self.gf('django.db.models.fields.IntegerField')()),
            ('practica', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador12', ['ManejoSuelo'])

        # Adding M2M table for field preparan on 'ManejoSuelo'
        db.create_table('indicador12_manejosuelo_preparan', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['indicador12.manejosuelo'], null=False)),
            ('preparar', models.ForeignKey(orm['indicador12.preparar'], null=False))
        ))
        db.create_unique('indicador12_manejosuelo_preparan', ['manejosuelo_id', 'preparar_id'])

        # Adding M2M table for field traccion on 'ManejoSuelo'
        db.create_table('indicador12_manejosuelo_traccion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['indicador12.manejosuelo'], null=False)),
            ('traccion', models.ForeignKey(orm['indicador12.traccion'], null=False))
        ))
        db.create_unique('indicador12_manejosuelo_traccion', ['manejosuelo_id', 'traccion_id'])

        # Adding M2M table for field fertilizacion on 'ManejoSuelo'
        db.create_table('indicador12_manejosuelo_fertilizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['indicador12.manejosuelo'], null=False)),
            ('fertilizacion', models.ForeignKey(orm['indicador12.fertilizacion'], null=False))
        ))
        db.create_unique('indicador12_manejosuelo_fertilizacion', ['manejosuelo_id', 'fertilizacion_id'])

        # Adding M2M table for field obra on 'ManejoSuelo'
        db.create_table('indicador12_manejosuelo_obra', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manejosuelo', models.ForeignKey(orm['indicador12.manejosuelo'], null=False)),
            ('conservacion', models.ForeignKey(orm['indicador12.conservacion'], null=False))
        ))
        db.create_unique('indicador12_manejosuelo_obra', ['manejosuelo_id', 'conservacion_id'])


    def backwards(self, orm):
        
        # Deleting model 'Textura'
        db.delete_table('indicador12_textura')

        # Deleting model 'Profundidad'
        db.delete_table('indicador12_profundidad')

        # Deleting model 'Densidad'
        db.delete_table('indicador12_densidad')

        # Deleting model 'Pendiente'
        db.delete_table('indicador12_pendiente')

        # Deleting model 'Drenaje'
        db.delete_table('indicador12_drenaje')

        # Deleting model 'Suelo'
        db.delete_table('indicador12_suelo')

        # Removing M2M table for field textura on 'Suelo'
        db.delete_table('indicador12_suelo_textura')

        # Removing M2M table for field profundidad on 'Suelo'
        db.delete_table('indicador12_suelo_profundidad')

        # Removing M2M table for field lombrices on 'Suelo'
        db.delete_table('indicador12_suelo_lombrices')

        # Removing M2M table for field densidad on 'Suelo'
        db.delete_table('indicador12_suelo_densidad')

        # Removing M2M table for field pendiente on 'Suelo'
        db.delete_table('indicador12_suelo_pendiente')

        # Removing M2M table for field drenaje on 'Suelo'
        db.delete_table('indicador12_suelo_drenaje')

        # Removing M2M table for field materia on 'Suelo'
        db.delete_table('indicador12_suelo_materia')

        # Deleting model 'Preparar'
        db.delete_table('indicador12_preparar')

        # Deleting model 'Traccion'
        db.delete_table('indicador12_traccion')

        # Deleting model 'Fertilizacion'
        db.delete_table('indicador12_fertilizacion')

        # Deleting model 'Conservacion'
        db.delete_table('indicador12_conservacion')

        # Deleting model 'ManejoSuelo'
        db.delete_table('indicador12_manejosuelo')

        # Removing M2M table for field preparan on 'ManejoSuelo'
        db.delete_table('indicador12_manejosuelo_preparan')

        # Removing M2M table for field traccion on 'ManejoSuelo'
        db.delete_table('indicador12_manejosuelo_traccion')

        # Removing M2M table for field fertilizacion on 'ManejoSuelo'
        db.delete_table('indicador12_manejosuelo_fertilizacion')

        # Removing M2M table for field obra on 'ManejoSuelo'
        db.delete_table('indicador12_manejosuelo_obra')


    models = {
        'indicador12.conservacion': {
            'Meta': {'object_name': 'Conservacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.densidad': {
            'Meta': {'object_name': 'Densidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.drenaje': {
            'Meta': {'object_name': 'Drenaje'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.fertilizacion': {
            'Meta': {'object_name': 'Fertilizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.manejosuelo': {
            'Meta': {'object_name': 'ManejoSuelo'},
            'analisis': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'fertilizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Fertilizacion']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Conservacion']", 'symmetrical': 'False'}),
            'practica': ('django.db.models.fields.IntegerField', [], {}),
            'preparan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Preparar']", 'symmetrical': 'False'}),
            'traccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Traccion']", 'symmetrical': 'False'})
        },
        'indicador12.pendiente': {
            'Meta': {'object_name': 'Pendiente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.preparar': {
            'Meta': {'object_name': 'Preparar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.profundidad': {
            'Meta': {'object_name': 'Profundidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.suelo': {
            'Meta': {'object_name': 'Suelo'},
            'densidad': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'densidad'", 'symmetrical': 'False', 'to': "orm['indicador12.Densidad']"}),
            'drenaje': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Drenaje']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lombrices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'lombrices'", 'symmetrical': 'False', 'to': "orm['indicador12.Densidad']"}),
            'materia': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'materia'", 'symmetrical': 'False', 'to': "orm['indicador12.Densidad']"}),
            'pendiente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Pendiente']", 'symmetrical': 'False'}),
            'profundidad': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Profundidad']", 'symmetrical': 'False'}),
            'textura': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador12.Textura']", 'symmetrical': 'False'})
        },
        'indicador12.textura': {
            'Meta': {'object_name': 'Textura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador12.traccion': {
            'Meta': {'object_name': 'Traccion'},
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

    complete_apps = ['indicador12']
