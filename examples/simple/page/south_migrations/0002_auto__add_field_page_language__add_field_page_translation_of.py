# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.language'
        db.add_column(u'page_page', u'language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=10),
                      keep_default=False)

        # Adding field 'Page.translation_of'
        db.add_column(u'page_page', u'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'translations', null=True, to=orm['page.Page']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.language'
        db.delete_column(u'page_page', u'language')

        # Deleting field 'Page.translation_of'
        db.delete_column(u'page_page', u'translation_of_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fobi.formentry': {
            'Meta': {'unique_together': "(('user', 'slug'), ('user', 'name'))", 'object_name': 'FormEntry'},
            'form_wizard_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormWizardEntry']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cloneable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'fobi.formwizardentry': {
            'Meta': {'unique_together': "(('user', 'slug'), ('user', 'name'))", 'object_name': 'FormWizardEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cloneable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'page.fobiformwidget': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'FobiFormWidget', 'db_table': "u'page_page_fobiformwidget'"},
            'form_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormEntry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fobiformwidget_set'", 'to': u"orm['page.Page']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'page.page': {
            'Meta': {'ordering': "[u'tree_id', u'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'db_index': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '10'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['page.Page']"}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            u'template_key': ('django.db.models.fields.CharField', [], {'default': "'page_base'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'translations'", 'null': 'True', 'to': u"orm['page.Page']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['page']