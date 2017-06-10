# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FormField'
        db.create_table(u'demo_formfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('choices', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='form_fields', to=orm['demo.FormPage'])),
        ))
        db.send_create_signal(u'demo', ['FormField'])

        # Adding model 'FormPage'
        db.create_table(u'demo_formpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wagtailcore.Page'], unique=True, primary_key=True)),
            ('to_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('from_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('intro', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
            ('thank_you_text', self.gf('wagtail.wagtailcore.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'demo', ['FormPage'])


    def backwards(self, orm):
        # Deleting model 'FormField'
        db.delete_table(u'demo_formfield')

        # Deleting model 'FormPage'
        db.delete_table(u'demo_formpage')


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
        u'demo.advert': {
            'Meta': {'object_name': 'Advert'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'adverts'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'demo.advertplacement': {
            'Meta': {'object_name': 'AdvertPlacement'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['demo.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'advert_placements'", 'to': u"orm['wagtailcore.Page']"})
        },
        u'demo.blogindexpage': {
            'Meta': {'object_name': 'BlogIndexPage', '_ormbases': [u'wagtailcore.Page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.blogindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.BlogIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.blogpage': {
            'Meta': {'object_name': 'BlogPage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.blogpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.BlogPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.blogpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'BlogPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.BlogPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.blogpagetag': {
            'Meta': {'object_name': 'BlogPageTag'},
            'content_object': ('modelcluster.fields.ParentalKey', [], {'related_name': "'tagged_items'", 'to': u"orm['demo.BlogPage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'demo_blogpagetag_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'demo.contactpage': {
            'Meta': {'object_name': 'ContactPage', '_ormbases': [u'wagtailcore.Page']},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'demo.eventindexpage': {
            'Meta': {'object_name': 'EventIndexPage', '_ormbases': [u'wagtailcore.Page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.eventindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.EventIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.eventpage': {
            'Meta': {'object_name': 'EventPage', '_ormbases': [u'wagtailcore.Page']},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'signup_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'time_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.eventpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.eventpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.eventpagespeaker': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventPageSpeaker'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'speakers'", 'to': u"orm['demo.EventPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.formfield': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'FormField'},
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'form_fields'", 'to': u"orm['demo.FormPage']"}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.formpage': {
            'Meta': {'object_name': 'FormPage'},
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'thank_you_text': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'demo.homepage': {
            'Meta': {'object_name': 'HomePage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.homepagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.HomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.homepagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.HomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.personpage': {
            'Meta': {'object_name': 'PersonPage', '_ormbases': [u'wagtailcore.Page']},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'biography': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'demo.personpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'PersonPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.PersonPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.standardindexpage': {
            'Meta': {'object_name': 'StandardIndexPage', '_ormbases': [u'wagtailcore.Page']},
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.standardindexpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.StandardIndexPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo.standardpage': {
            'Meta': {'object_name': 'StandardPage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.standardpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageCarouselItem'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'embed_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['wagtailimages.Image']"}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['demo.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'demo.standardpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'link_external': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['demo.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'wagtailcore.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'has_unpublished_changes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_pages'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'search_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'wagtaildocs.document': {
            'Meta': {'object_name': 'Document'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'wagtailimages.image': {
            'Meta': {'object_name': 'Image'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uploaded_by_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['demo']