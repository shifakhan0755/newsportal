# Generated by Django 3.1.4 on 2021-06-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('abouttxt', models.TextField(default='')),
                ('fb', models.CharField(default='-', max_length=50)),
                ('tw', models.CharField(default='-', max_length=50)),
                ('yt', models.CharField(default='-', max_length=50)),
                ('tell', models.CharField(default='-', max_length=50)),
                ('link', models.CharField(default='-', max_length=50)),
                ('set_name', models.CharField(default='-', max_length=50)),
                ('picurl', models.TextField(default='')),
                ('picname', models.TextField(default='')),
                ('picurl2', models.TextField(default='')),
                ('picname2', models.TextField(default='')),
            ],
        ),
    ]
