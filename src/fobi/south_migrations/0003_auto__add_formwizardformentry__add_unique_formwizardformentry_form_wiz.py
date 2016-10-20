# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FormWizardFormEntry'
        db.create_table(u'fobi_formwizardformentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_wizard_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormWizardEntry'])),
            ('form_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormEntry'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fobi', ['FormWizardFormEntry'])

        # Adding unique constraint on 'FormWizardFormEntry', fields ['form_wizard_entry', 'form_entry']
        db.create_unique(u'fobi_formwizardformentry', ['form_wizard_entry_id', 'form_entry_id'])

        # Adding model 'FormWizardHandlerEntry'
        db.create_table(u'fobi_formwizardhandlerentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plugin_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('form_wizard_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormWizardEntry'])),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'fobi', ['FormWizardHandlerEntry'])

        # Adding model 'FormWizardHandler'
        db.create_table(u'fobi_formwizardhandler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'fobi', ['FormWizardHandler'])

        # Adding M2M table for field users on 'FormWizardHandler'
        m2m_table_name = db.shorten_name(u'fobi_formwizardhandler_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formwizardhandler', models.ForeignKey(orm[u'fobi.formwizardhandler'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formwizardhandler_id', 'user_id'])

        # Adding M2M table for field groups on 'FormWizardHandler'
        m2m_table_name = db.shorten_name(u'fobi_formwizardhandler_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formwizardhandler', models.ForeignKey(orm[u'fobi.formwizardhandler'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formwizardhandler_id', 'group_id'])

        # Deleting field 'FormEntry.position'
        db.delete_column(u'fobi_formentry', 'position')

        # Deleting field 'FormEntry.form_wizard_entry'
        db.delete_column(u'fobi_formentry', 'form_wizard_entry_id')

        # Adding field 'FormWizardEntry.success_page_title'
        db.add_column(u'fobi_formwizardentry', 'success_page_title',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FormWizardEntry.success_page_message'
        db.add_column(u'fobi_formwizardentry', 'success_page_message',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FormWizardEntry.wizard_type'
        db.add_column(u'fobi_formwizardentry', 'wizard_type',
                      self.gf('django.db.models.fields.CharField')(default='SessionWizardView', max_length=255),
                      keep_default=False)

        # Adding field 'FormWizardEntry.created'
        db.add_column(u'fobi_formwizardentry', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FormWizardEntry.updated'
        db.add_column(u'fobi_formwizardentry', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'FormWizardFormEntry', fields ['form_wizard_entry', 'form_entry']
        db.delete_unique(u'fobi_formwizardformentry', ['form_wizard_entry_id', 'form_entry_id'])

        # Deleting model 'FormWizardFormEntry'
        db.delete_table(u'fobi_formwizardformentry')

        # Deleting model 'FormWizardHandlerEntry'
        db.delete_table(u'fobi_formwizardhandlerentry')

        # Deleting model 'FormWizardHandler'
        db.delete_table(u'fobi_formwizardhandler')

        # Removing M2M table for field users on 'FormWizardHandler'
        db.delete_table(db.shorten_name(u'fobi_formwizardhandler_users'))

        # Removing M2M table for field groups on 'FormWizardHandler'
        db.delete_table(db.shorten_name(u'fobi_formwizardhandler_groups'))

        # Adding field 'FormEntry.position'
        db.add_column(u'fobi_formentry', 'position',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FormEntry.form_wizard_entry'
        db.add_column(u'fobi_formentry', 'form_wizard_entry',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormWizardEntry'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'FormWizardEntry.success_page_title'
        db.delete_column(u'fobi_formwizardentry', 'success_page_title')

        # Deleting field 'FormWizardEntry.success_page_message'
        db.delete_column(u'fobi_formwizardentry', 'success_page_message')

        # Deleting field 'FormWizardEntry.wizard_type'
        db.delete_column(u'fobi_formwizardentry', 'wizard_type')

        # Deleting field 'FormWizardEntry.created'
        db.delete_column(u'fobi_formwizardentry', 'created')

        # Deleting field 'FormWizardEntry.updated'
        db.delete_column(u'fobi_formwizardentry', 'updated')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fobi.formelement': {
            'Meta': {'object_name': 'FormElement'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'fobi.formelemententry': {
            'Meta': {'ordering': "['position']", 'object_name': 'FormElementEntry'},
            'form_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormEntry']"}),
            'form_fieldset_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormFieldsetEntry']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fobi.formentry': {
            'Meta': {'unique_together': "(('user', 'slug'), ('user', 'name'))", 'object_name': 'FormEntry'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cloneable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'success_page_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'success_page_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'fobi.formfieldsetentry': {
            'Meta': {'unique_together': "(('form_entry', 'name'),)", 'object_name': 'FormFieldsetEntry'},
            'form_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormEntry']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_repeatable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'fobi.formhandler': {
            'Meta': {'object_name': 'FormHandler'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'fobi.formhandlerentry': {
            'Meta': {'object_name': 'FormHandlerEntry'},
            'form_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormEntry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'fobi.formwizardentry': {
            'Meta': {'unique_together': "(('user', 'slug'), ('user', 'name'))", 'object_name': 'FormWizardEntry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cloneable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'success_page_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'success_page_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'wizard_type': ('django.db.models.fields.CharField', [], {'default': "'SessionWizardView'", 'max_length': '255'})
        },
        u'fobi.formwizardformentry': {
            'Meta': {'ordering': "['position']", 'unique_together': "(('form_wizard_entry', 'form_entry'),)", 'object_name': 'FormWizardFormEntry'},
            'form_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormEntry']"}),
            'form_wizard_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormWizardEntry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fobi.formwizardhandler': {
            'Meta': {'object_name': 'FormWizardHandler'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'fobi.formwizardhandlerentry': {
            'Meta': {'object_name': 'FormWizardHandlerEntry'},
            'form_wizard_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormWizardEntry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['fobi']