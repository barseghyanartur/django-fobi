# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FormElement'
        db.create_table(u'fobi_formelement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'fobi', ['FormElement'])

        # Adding M2M table for field users on 'FormElement'
        m2m_table_name = db.shorten_name(u'fobi_formelement_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formelement', models.ForeignKey(orm[u'fobi.formelement'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formelement_id', 'user_id'])

        # Adding M2M table for field groups on 'FormElement'
        m2m_table_name = db.shorten_name(u'fobi_formelement_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formelement', models.ForeignKey(orm[u'fobi.formelement'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formelement_id', 'group_id'])

        # Adding model 'FormHandler'
        db.create_table(u'fobi_formhandler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'fobi', ['FormHandler'])

        # Adding M2M table for field users on 'FormHandler'
        m2m_table_name = db.shorten_name(u'fobi_formhandler_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formhandler', models.ForeignKey(orm[u'fobi.formhandler'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formhandler_id', 'user_id'])

        # Adding M2M table for field groups on 'FormHandler'
        m2m_table_name = db.shorten_name(u'fobi_formhandler_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formhandler', models.ForeignKey(orm[u'fobi.formhandler'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formhandler_id', 'group_id'])

        # Adding model 'FormWizardEntry'
        db.create_table(u'fobi_formwizardentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_cloneable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'fobi', ['FormWizardEntry'])

        # Adding unique constraint on 'FormWizardEntry', fields ['user', 'slug']
        db.create_unique(u'fobi_formwizardentry', ['user_id', 'slug'])

        # Adding unique constraint on 'FormWizardEntry', fields ['user', 'name']
        db.create_unique(u'fobi_formwizardentry', ['user_id', 'name'])

        # Adding model 'FormEntry'
        db.create_table(u'fobi_formentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_wizard_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormWizardEntry'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_cloneable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('success_page_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('success_page_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'fobi', ['FormEntry'])

        # Adding unique constraint on 'FormEntry', fields ['user', 'slug']
        db.create_unique(u'fobi_formentry', ['user_id', 'slug'])

        # Adding unique constraint on 'FormEntry', fields ['user', 'name']
        db.create_unique(u'fobi_formentry', ['user_id', 'name'])

        # Adding model 'FormFieldsetEntry'
        db.create_table(u'fobi_formfieldsetentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormEntry'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_repeatable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'fobi', ['FormFieldsetEntry'])

        # Adding unique constraint on 'FormFieldsetEntry', fields ['form_entry', 'name']
        db.create_unique(u'fobi_formfieldsetentry', ['form_entry_id', 'name'])

        # Adding model 'FormElementEntry'
        db.create_table(u'fobi_formelemententry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormEntry'])),
            ('plugin_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('form_fieldset_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormFieldsetEntry'], null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fobi', ['FormElementEntry'])

        # Adding model 'FormHandlerEntry'
        db.create_table(u'fobi_formhandlerentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fobi.FormEntry'])),
            ('plugin_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'fobi', ['FormHandlerEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'FormFieldsetEntry', fields ['form_entry', 'name']
        db.delete_unique(u'fobi_formfieldsetentry', ['form_entry_id', 'name'])

        # Removing unique constraint on 'FormEntry', fields ['user', 'name']
        db.delete_unique(u'fobi_formentry', ['user_id', 'name'])

        # Removing unique constraint on 'FormEntry', fields ['user', 'slug']
        db.delete_unique(u'fobi_formentry', ['user_id', 'slug'])

        # Removing unique constraint on 'FormWizardEntry', fields ['user', 'name']
        db.delete_unique(u'fobi_formwizardentry', ['user_id', 'name'])

        # Removing unique constraint on 'FormWizardEntry', fields ['user', 'slug']
        db.delete_unique(u'fobi_formwizardentry', ['user_id', 'slug'])

        # Deleting model 'FormElement'
        db.delete_table(u'fobi_formelement')

        # Removing M2M table for field users on 'FormElement'
        db.delete_table(db.shorten_name(u'fobi_formelement_users'))

        # Removing M2M table for field groups on 'FormElement'
        db.delete_table(db.shorten_name(u'fobi_formelement_groups'))

        # Deleting model 'FormHandler'
        db.delete_table(u'fobi_formhandler')

        # Removing M2M table for field users on 'FormHandler'
        db.delete_table(db.shorten_name(u'fobi_formhandler_users'))

        # Removing M2M table for field groups on 'FormHandler'
        db.delete_table(db.shorten_name(u'fobi_formhandler_groups'))

        # Deleting model 'FormWizardEntry'
        db.delete_table(u'fobi_formwizardentry')

        # Deleting model 'FormEntry'
        db.delete_table(u'fobi_formentry')

        # Deleting model 'FormFieldsetEntry'
        db.delete_table(u'fobi_formfieldsetentry')

        # Deleting model 'FormElementEntry'
        db.delete_table(u'fobi_formelemententry')

        # Deleting model 'FormHandlerEntry'
        db.delete_table(u'fobi_formhandlerentry')


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
            'form_wizard_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fobi.FormWizardEntry']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cloneable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'success_page_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'success_page_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cloneable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['fobi']