# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0021_auto_20160328_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghour',
            name='weekday',
            field=models.SmallIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')]),
        ),
    ]
