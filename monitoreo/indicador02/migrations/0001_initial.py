# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OrgGremiales'
        db.create_table('indicador02_orggremiales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador02', ['OrgGremiales'])

        # Adding model 'BeneficiosObtenido'
        db.create_table('indicador02_beneficiosobtenido', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador02', ['BeneficiosObtenido'])

        # Adding model 'SerMiembro'
        db.create_table('indicador02_sermiembro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador02', ['SerMiembro'])

        # Adding model 'OrganizacionGremial'
        db.create_table('indicador02_organizaciongremial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desde_socio', self.gf('django.db.models.fields.IntegerField')()),
            ('miembro_gremial', self.gf('django.db.models.fields.IntegerField')()),
            ('desde_miembro', self.gf('django.db.models.fields.IntegerField')()),
            ('capacitacion', self.gf('django.db.models.fields.IntegerField')()),
            ('desde_capacitacion', self.gf('django.db.models.fields.IntegerField')()),
            ('asumir_cargo', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador02', ['OrganizacionGremial'])

        # Adding M2M table for field socio on 'OrganizacionGremial'
        db.create_table('indicador02_organizaciongremial_socio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm['indicador02.organizaciongremial'], null=False)),
            ('orggremiales', models.ForeignKey(orm['indicador02.orggremiales'], null=False))
        ))
        db.create_unique('indicador02_organizaciongremial_socio', ['organizaciongremial_id', 'orggremiales_id'])

        # Adding M2M table for field beneficio on 'OrganizacionGremial'
        db.create_table('indicador02_organizaciongremial_beneficio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm['indicador02.organizaciongremial'], null=False)),
            ('beneficiosobtenido', models.ForeignKey(orm['indicador02.beneficiosobtenido'], null=False))
        ))
        db.create_unique('indicador02_organizaciongremial_beneficio', ['organizaciongremial_id', 'beneficiosobtenido_id'])

        # Adding M2M table for field miembro_junta on 'OrganizacionGremial'
        db.create_table('indicador02_organizaciongremial_miembro_junta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm['indicador02.organizaciongremial'], null=False)),
            ('sermiembro', models.ForeignKey(orm['indicador02.sermiembro'], null=False))
        ))
        db.create_unique('indicador02_organizaciongremial_miembro_junta', ['organizaciongremial_id', 'sermiembro_id'])

        # Adding model 'OrgComunitarias'
        db.create_table('indicador02_orgcomunitarias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador02', ['OrgComunitarias'])

        # Adding model 'BeneficioOrgComunitaria'
        db.create_table('indicador02_beneficioorgcomunitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador02', ['BeneficioOrgComunitaria'])

        # Adding model 'NoOrganizado'
        db.create_table('indicador02_noorganizado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('indicador02', ['NoOrganizado'])

        # Adding model 'OrganizacionComunitaria'
        db.create_table('indicador02_organizacioncomunitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('pertence', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simas.Encuesta'])),
        ))
        db.send_create_signal('indicador02', ['OrganizacionComunitaria'])

        # Adding M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.create_table('indicador02_organizacioncomunitaria_cual_organizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['indicador02.organizacioncomunitaria'], null=False)),
            ('orgcomunitarias', models.ForeignKey(orm['indicador02.orgcomunitarias'], null=False))
        ))
        db.create_unique('indicador02_organizacioncomunitaria_cual_organizacion', ['organizacioncomunitaria_id', 'orgcomunitarias_id'])

        # Adding M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.create_table('indicador02_organizacioncomunitaria_cual_beneficio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['indicador02.organizacioncomunitaria'], null=False)),
            ('beneficioorgcomunitaria', models.ForeignKey(orm['indicador02.beneficioorgcomunitaria'], null=False))
        ))
        db.create_unique('indicador02_organizacioncomunitaria_cual_beneficio', ['organizacioncomunitaria_id', 'beneficioorgcomunitaria_id'])

        # Adding M2M table for field no_organizado on 'OrganizacionComunitaria'
        db.create_table('indicador02_organizacioncomunitaria_no_organizado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm['indicador02.organizacioncomunitaria'], null=False)),
            ('noorganizado', models.ForeignKey(orm['indicador02.noorganizado'], null=False))
        ))
        db.create_unique('indicador02_organizacioncomunitaria_no_organizado', ['organizacioncomunitaria_id', 'noorganizado_id'])


    def backwards(self, orm):
        
        # Deleting model 'OrgGremiales'
        db.delete_table('indicador02_orggremiales')

        # Deleting model 'BeneficiosObtenido'
        db.delete_table('indicador02_beneficiosobtenido')

        # Deleting model 'SerMiembro'
        db.delete_table('indicador02_sermiembro')

        # Deleting model 'OrganizacionGremial'
        db.delete_table('indicador02_organizaciongremial')

        # Removing M2M table for field socio on 'OrganizacionGremial'
        db.delete_table('indicador02_organizaciongremial_socio')

        # Removing M2M table for field beneficio on 'OrganizacionGremial'
        db.delete_table('indicador02_organizaciongremial_beneficio')

        # Removing M2M table for field miembro_junta on 'OrganizacionGremial'
        db.delete_table('indicador02_organizaciongremial_miembro_junta')

        # Deleting model 'OrgComunitarias'
        db.delete_table('indicador02_orgcomunitarias')

        # Deleting model 'BeneficioOrgComunitaria'
        db.delete_table('indicador02_beneficioorgcomunitaria')

        # Deleting model 'NoOrganizado'
        db.delete_table('indicador02_noorganizado')

        # Deleting model 'OrganizacionComunitaria'
        db.delete_table('indicador02_organizacioncomunitaria')

        # Removing M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.delete_table('indicador02_organizacioncomunitaria_cual_organizacion')

        # Removing M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.delete_table('indicador02_organizacioncomunitaria_cual_beneficio')

        # Removing M2M table for field no_organizado on 'OrganizacionComunitaria'
        db.delete_table('indicador02_organizacioncomunitaria_no_organizado')


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
        'indicador02.beneficioorgcomunitaria': {
            'Meta': {'object_name': 'BeneficioOrgComunitaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador02.beneficiosobtenido': {
            'Meta': {'object_name': 'BeneficiosObtenido'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador02.noorganizado': {
            'Meta': {'object_name': 'NoOrganizado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador02.organizacioncomunitaria': {
            'Meta': {'object_name': 'OrganizacionComunitaria'},
            'cual_beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador02.BeneficioOrgComunitaria']", 'symmetrical': 'False'}),
            'cual_organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador02.OrgComunitarias']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador02.NoOrganizado']", 'symmetrical': 'False'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'pertence': ('django.db.models.fields.IntegerField', [], {})
        },
        'indicador02.organizaciongremial': {
            'Meta': {'object_name': 'OrganizacionGremial'},
            'asumir_cargo': ('django.db.models.fields.IntegerField', [], {}),
            'beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador02.BeneficiosObtenido']", 'symmetrical': 'False'}),
            'capacitacion': ('django.db.models.fields.IntegerField', [], {}),
            'desde_capacitacion': ('django.db.models.fields.IntegerField', [], {}),
            'desde_miembro': ('django.db.models.fields.IntegerField', [], {}),
            'desde_socio': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simas.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miembro_gremial': ('django.db.models.fields.IntegerField', [], {}),
            'miembro_junta': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador02.SerMiembro']", 'symmetrical': 'False'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['indicador02.OrgGremiales']", 'symmetrical': 'False'})
        },
        'indicador02.orgcomunitarias': {
            'Meta': {'object_name': 'OrgComunitarias'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador02.orggremiales': {
            'Meta': {'object_name': 'OrgGremiales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indicador02.sermiembro': {
            'Meta': {'object_name': 'SerMiembro'},
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

    complete_apps = ['indicador02']
