# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0020_auto_20160328_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]