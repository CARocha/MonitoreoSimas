# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Educacion'
        db.create_table('indicador01_educacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('no_leer', self.gf('django.db.models.fields.IntegerField')()),
            ('p_incompleta', self.gf('django.db.models.fields.IntegerField')()),
            ('p_completa', self.gf('django.db.models.fields.IntegerField')()),
            ('s_incompleta', self.gf('django.db.models.fields.IntegerField')()),
            ('bachiller', self.gf('django.db.models.fields.IntegerField')()),
            ('universitario', self.gf('django.db.models.fields.IntegerField')()),
            ('f_comunidad', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador01', ['Educacion'])

        # Adding model 'Salud'
        db.create_table('indicador01_salud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('b_salud', self.gf('django.db.models.fields.IntegerField')()),
            ('s_delicada', self.gf('django.db.models.fields.IntegerField')()),
            ('e_cronica', self.gf('django.db.models.fields.IntegerField')()),
            ('v_centro', self.gf('django.db.models.fields.IntegerField')()),
            ('v_medico', self.gf('django.db.models.fields.IntegerField')()),
            ('v_naturista', self.gf('django.db.models.fields.IntegerField')()),
            ('automedica', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador01', ['Salud'])

        # Adding model 'PreguntaEnergia'
        db.create_table('indicador01_preguntaenergia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador01', ['PreguntaEnergia'])

        # Adding model 'Energia'
        db.create_table('indicador01_energia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador01.PreguntaEnergia'])),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador01', ['Energia'])

        # Adding model 'TipoCocina'
        db.create_table('indicador01_tipococina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador01', ['TipoCocina'])

        # Adding model 'Cocina'
        db.create_table('indicador01_cocina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador01', ['Cocina'])

        # Adding M2M table for field utiliza on 'Cocina'
        db.create_table('indicador01_cocina_utiliza', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cocina', models.ForeignKey(orm['indicador01.cocina'], null=False)),
            ('tipococina', models.ForeignKey(orm['indicador01.tipococina'], null=False))
        ))
        db.create_unique('indicador01_cocina_utiliza', ['cocina_id', 'tipococina_id'])

        # Adding model 'Fuente'
        db.create_table('indicador01_fuente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador01', ['Fuente'])

        # Adding model 'Tratamiento'
        db.create_table('indicador01_tratamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador01', ['Tratamiento'])

        # Adding model 'Disponibilidad'
        db.create_table('indicador01_disponibilidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador01', ['Disponibilidad'])

        # Adding model 'Agua'
        db.create_table('indicador01_agua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador01', ['Agua'])

        # Adding M2M table for field fuente on 'Agua'
        db.create_table('indicador01_agua_fuente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agua', models.ForeignKey(orm['indicador01.agua'], null=False)),
            ('fuente', models.ForeignKey(orm['indicador01.fuente'], null=False))
        ))
        db.create_unique('indicador01_agua_fuente', ['agua_id', 'fuente_id'])

        # Adding M2M table for field trata on 'Agua'
        db.create_table('indicador01_agua_trata', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agua', models.ForeignKey(orm['indicador01.agua'], null=False)),
            ('tratamiento', models.ForeignKey(orm['indicador01.tratamiento'], null=False))
        ))
        db.create_unique('indicador01_agua_trata', ['agua_id', 'tratamiento_id'])

        # Adding M2M table for field disponible on 'Agua'
        db.create_table('indicador01_agua_disponible', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('agua', models.ForeignKey(orm['indicador01.agua'], null=False)),
            ('disponibilidad', models.ForeignKey(orm['indicador01.disponibilidad'], null=False))
        ))
        db.create_unique('indicador01_agua_disponible', ['agua_id', 'disponibilidad_id'])


    def backwards(self, orm):
        
        # Deleting model 'Educacion'
        db.delete_table('indicador01_educacion')

        # Deleting model 'Salud'
        db.delete_table('indicador01_salud')

        # Deleting model 'PreguntaEnergia'
        db.delete_table('indicador01_preguntaenergia')

        # Deleting model 'Energia'
        db.delete_table('indicador01_energia')

        # Deleting model 'TipoCocina'
        db.delete_table('indicador01_tipococina')

        # Deleting model 'Cocina'
        db.delete_table('indicador01_cocina')

        # Removing M2M table for field utiliza on 'Cocina'
        db.delete_table('indicador01_cocina_utiliza')

        # Deleting model 'Fuente'
        db.delete_table('indicador01_fuente')

        # Deleting model 'Tratamiento'
        db.delete_table('indicador01_tratamiento')

        # Deleting model 'Disponibilidad'
        db.delete_table('indicador01_disponibilidad')

        # Deleting model 'Agua'
        db.delete_table('indicador01_agua')

        # Removing M2M table for field fuente on 'Agua'
        db.delete_table('indicador01_agua_fuente')

        # Removing M2M table for field trata on 'Agua'
        db.delete_table('indicador01_agua_trata')

        # Removing M2M table for field disponible on 'Agua'
        db.delete_table('indicador01_agua_disponible')


    models = {
        'indicador01.agua': {
            'Meta': {'object_name': 'Agua'},
            'disponible': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador01.Disponibilidad']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador01.Fuente']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trata': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador01.Tratamiento']", 'symmetrical': 'False'})
        },
        'indicador01.cocina': {
            'Meta': {'object_name': 'Cocina'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utiliza': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['indicador01.TipoCocina']", 'null': 'True', 'blank': 'True'})
        },
        'indicador01.disponibilidad': {
            'Meta': {'object_name': 'Disponibilidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador01.educacion': {
            'Meta': {'object_name': 'Educacion'},
            'bachiller': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'f_comunidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_leer': ('django.db.models.fields.IntegerField', [], {}),
            'p_completa': ('django.db.models.fields.IntegerField', [], {}),
            'p_incompleta': ('django.db.models.fields.IntegerField', [], {}),
            's_incompleta': ('django.db.models.fields.IntegerField', [], {}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {}),
            'universitario': ('django.db.models.fields.IntegerField', [], {})
        },
        'indicador01.energia': {
            'Meta': {'object_name': 'Energia'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador01.PreguntaEnergia']"}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'indicador01.fuente': {
            'Meta': {'object_name': 'Fuente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador01.preguntaenergia': {
            'Meta': {'object_name': 'PreguntaEnergia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador01.salud': {
            'Meta': {'object_name': 'Salud'},
            'automedica': ('django.db.models.fields.IntegerField', [], {}),
            'b_salud': ('django.db.models.fields.IntegerField', [], {}),
            'e_cronica': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            's_delicada': ('django.db.models.fields.IntegerField', [], {}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'v_centro': ('django.db.models.fields.IntegerField', [], {}),
            'v_medico': ('django.db.models.fields.IntegerField', [], {}),
            'v_naturista': ('django.db.models.fields.IntegerField', [], {})
        },
        'indicador01.tipococina': {
            'Meta': {'object_name': 'TipoCocina'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador01.tratamiento': {
            'Meta': {'object_name': 'Tratamiento'},
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

    complete_apps = ['indicador01']
