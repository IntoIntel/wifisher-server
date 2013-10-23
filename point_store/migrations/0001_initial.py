# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataPoint'
        db.create_table('point_store_datapoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
            ('accuracy', self.gf('django.db.models.fields.FloatField')()),
            ('altitude', self.gf('django.db.models.fields.FloatField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('frequency', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('ssid', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('bssid', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('capabilities', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('point_store', ['DataPoint'])


    def backwards(self, orm):
        # Deleting model 'DataPoint'
        db.delete_table('point_store_datapoint')


    models = {
        'point_store.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            'accuracy': ('django.db.models.fields.FloatField', [], {}),
            'altitude': ('django.db.models.fields.FloatField', [], {}),
            'bssid': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'capabilities': ('django.db.models.fields.TextField', [], {}),
            'frequency': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'speed': ('django.db.models.fields.FloatField', [], {}),
            'ssid': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['point_store']