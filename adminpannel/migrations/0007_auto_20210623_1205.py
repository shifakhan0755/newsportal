# Generated by Django 3.1.4 on 2021-06-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0006_auto_20210622_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AlterField(
            model_name='main',
            name='email',
            field=models.EmailField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='lin',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='tell',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
    ]