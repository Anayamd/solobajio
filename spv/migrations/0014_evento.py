# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0013_auto_20160327_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=50)),
                ('decription', models.TextField()),
            ],
        ),
    ]
