# Generated by Django 3.1.4 on 2021-05-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_image', models.ImageField(blank=True, upload_to='home/static/media')),
                ('s_vedio', models.FileField(blank=True, upload_to='vedio/%y')),
            ],
        ),
    ]
