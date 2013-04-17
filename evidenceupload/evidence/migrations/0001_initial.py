# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Evidence'
        db.create_table(u'evidence_evidence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fpfile', self.gf('django_filepicker.models.FPFileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
        ))
        db.send_create_signal(u'evidence', ['Evidence'])


    def backwards(self, orm):
        # Deleting model 'Evidence'
        db.delete_table(u'evidence_evidence')


    models = {
        u'evidence.evidence': {
            'Meta': {'object_name': 'Evidence'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'fpfile': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['evidence']