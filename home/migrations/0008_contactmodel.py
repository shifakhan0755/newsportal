# Generated by Django 3.1.4 on 2021-05-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_worldmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.TextField(max_length=100)),
                ('comment', models.TextField(max_length=2000)),
            ],
        ),
    ]
