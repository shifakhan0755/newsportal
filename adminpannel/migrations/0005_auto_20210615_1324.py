# Generated by Django 3.1.4 on 2021-06-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0004_auto_20210614_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='set_name',
        ),
        migrations.AddField(
            model_name='main',
            name='email',
            field=models.EmailField(default='-', max_length=50),
        ),
    ]
