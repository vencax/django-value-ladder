# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Thing'
        db.create_table('valueladder_thing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('valueladder', ['Thing'])

        # Adding model 'ThingTranslation'
        db.create_table('valueladder_thingtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['valueladder.Thing'])),
            ('language_code', self.gf('django.db.models.fields.CharField')(default='ar', max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('valueladder', ['ThingTranslation'])

        # Adding model 'ThingValue'
        db.create_table('valueladder_thingvalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thingA', self.gf('django.db.models.fields.related.ForeignKey')(related_name='changing_things', to=orm['valueladder.Thing'])),
            ('thingB', self.gf('django.db.models.fields.related.ForeignKey')(related_name='changed_things', to=orm['valueladder.Thing'])),
            ('ratio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('valueladder', ['ThingValue'])

        # Adding unique constraint on 'ThingValue', fields ['thingA', 'thingB', 'ratio']
        db.create_unique('valueladder_thingvalue', ['thingA_id', 'thingB_id', 'ratio'])


    def backwards(self, orm):
        # Removing unique constraint on 'ThingValue', fields ['thingA', 'thingB', 'ratio']
        db.delete_unique('valueladder_thingvalue', ['thingA_id', 'thingB_id', 'ratio'])

        # Deleting model 'Thing'
        db.delete_table('valueladder_thing')

        # Deleting model 'ThingTranslation'
        db.delete_table('valueladder_thingtranslation')

        # Deleting model 'ThingValue'
        db.delete_table('valueladder_thingvalue')


    models = {
        'valueladder.thing': {
            'Meta': {'object_name': 'Thing'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'valueladder.thingtranslation': {
            'Meta': {'ordering': "['title']", 'object_name': 'ThingTranslation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "'ar'", 'max_length': '10'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['valueladder.Thing']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'valueladder.thingvalue': {
            'Meta': {'unique_together': "(('thingA', 'thingB', 'ratio'),)", 'object_name': 'ThingValue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.FloatField', [], {}),
            'thingA': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'changing_things'", 'to': "orm['valueladder.Thing']"}),
            'thingB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'changed_things'", 'to': "orm['valueladder.Thing']"})
        }
    }

    complete_apps = ['valueladder']