# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0009_negocio_ranking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OpeningHours',
            new_name='OpeningHour',
        ),
    ]