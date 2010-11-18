# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Piso'
        db.create_table('indicador15_piso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador15', ['Piso'])

        # Adding model 'Techo'
        db.create_table('indicador15_techo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador15', ['Techo'])

        # Adding model 'TipoCasa'
        db.create_table('indicador15_tipocasa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador15', ['TipoCasa'])

        # Adding M2M table for field piso on 'TipoCasa'
        db.create_table('indicador15_tipocasa_piso', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['indicador15.tipocasa'], null=False)),
            ('piso', models.ForeignKey(orm['indicador15.piso'], null=False))
        ))
        db.create_unique('indicador15_tipocasa_piso', ['tipocasa_id', 'piso_id'])

        # Adding M2M table for field techo on 'TipoCasa'
        db.create_table('indicador15_tipocasa_techo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tipocasa', models.ForeignKey(orm['indicador15.tipocasa'], null=False)),
            ('techo', models.ForeignKey(orm['indicador15.techo'], null=False))
        ))
        db.create_unique('indicador15_tipocasa_techo', ['tipocasa_id', 'techo_id'])

        # Adding model 'DetalleCasa'
        db.create_table('indicador15_detallecasa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tamano', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ambientes', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('letrina', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lavadero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador15', ['DetalleCasa'])

        # Adding model 'Equipos'
        db.create_table('indicador15_equipos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador15', ['Equipos'])

        # Adding model 'Infraestructuras'
        db.create_table('indicador15_infraestructuras', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador15', ['Infraestructuras'])

        # Adding model 'Propiedades'
        db.create_table('indicador15_propiedades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.Equipos'], null=True, blank=True)),
            ('cantidad_equipo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('infraestructura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.Infraestructuras'], null=True, blank=True)),
            ('cantidad_infra', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador15', ['Propiedades'])

        # Adding model 'NombreHerramienta'
        db.create_table('indicador15_nombreherramienta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador15', ['NombreHerramienta'])

        # Adding model 'Herramientas'
        db.create_table('indicador15_herramientas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('herramienta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.NombreHerramienta'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador15', ['Herramientas'])

        # Adding model 'NombreTransporte'
        db.create_table('indicador15_nombretransporte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indicador15', ['NombreTransporte'])

        # Adding model 'Transporte'
        db.create_table('indicador15_transporte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transporte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicador15.NombreTransporte'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador15', ['Transporte'])


    def backwards(self, orm):
        
        # Deleting model 'Piso'
        db.delete_table('indicador15_piso')

        # Deleting model 'Techo'
        db.delete_table('indicador15_techo')

        # Deleting model 'TipoCasa'
        db.delete_table('indicador15_tipocasa')

        # Removing M2M table for field piso on 'TipoCasa'
        db.delete_table('indicador15_tipocasa_piso')

        # Removing M2M table for field techo on 'TipoCasa'
        db.delete_table('indicador15_tipocasa_techo')

        # Deleting model 'DetalleCasa'
        db.delete_table('indicador15_detallecasa')

        # Deleting model 'Equipos'
        db.delete_table('indicador15_equipos')

        # Deleting model 'Infraestructuras'
        db.delete_table('indicador15_infraestructuras')

        # Deleting model 'Propiedades'
        db.delete_table('indicador15_propiedades')

        # Deleting model 'NombreHerramienta'
        db.delete_table('indicador15_nombreherramienta')

        # Deleting model 'Herramientas'
        db.delete_table('indicador15_herramientas')

        # Deleting model 'NombreTransporte'
        db.delete_table('indicador15_nombretransporte')

        # Deleting model 'Transporte'
        db.delete_table('indicador15_transporte')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.detallecasa': {
            'Meta': {'object_name': 'DetalleCasa'},
            'ambientes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lavadero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'letrina': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tamano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'indicador15.equipos': {
            'Meta': {'object_name': 'Equipos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.herramientas': {
            'Meta': {'object_name': 'Herramientas'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'herramienta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador15.NombreHerramienta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'indicador15.infraestructuras': {
            'Meta': {'object_name': 'Infraestructuras'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.nombreherramienta': {
            'Meta': {'object_name': 'NombreHerramienta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.nombretransporte': {
            'Meta': {'object_name': 'NombreTransporte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.piso': {
            'Meta': {'object_name': 'Piso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.propiedades': {
            'Meta': {'object_name': 'Propiedades'},
            'cantidad_equipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cantidad_infra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador15.Equipos']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infraestructura': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador15.Infraestructuras']", 'null': 'True', 'blank': 'True'})
        },
        'indicador15.techo': {
            'Meta': {'object_name': 'Techo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indicador15.tipocasa': {
            'Meta': {'object_name': 'TipoCasa'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'piso': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador15.Piso']", 'symmetrical': 'False'}),
            'techo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador15.Techo']", 'symmetrical': 'False'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'indicador15.transporte': {
            'Meta': {'object_name': 'Transporte'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transporte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicador15.NombreTransporte']"})
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
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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

    complete_apps = ['indicador15']
