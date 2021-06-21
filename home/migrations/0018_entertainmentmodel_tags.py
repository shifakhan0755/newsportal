# Generated by Django 3.1.4 on 2021-06-16 07:53

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('home', '0017_auto_20210607_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='entertainmentmodel',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
