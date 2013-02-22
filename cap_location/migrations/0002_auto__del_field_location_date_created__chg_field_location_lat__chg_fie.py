# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Location.date_created'
        db.delete_column('location_location', 'date_created')


        # Changing field 'Location.lat'
        db.alter_column('location_location', 'lat', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Location.lng'
        db.alter_column('location_location', 'lng', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Adding field 'Location.date_created'
        db.add_column('location_location', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)


        # Changing field 'Location.lat'
        db.alter_column('location_location', 'lat', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

        # Changing field 'Location.lng'
        db.alter_column('location_location', 'lng', self.gf('django.db.models.fields.CharField')(default=None, max_length=255))

    models = {
        'location.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['location']