# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import spv.models


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0007_auto_20160323_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='icon',
            field=models.ImageField(upload_to='img/industry/'),
        ),
        migrations.AlterField(
            model_name='negocioimg',
            name='image',
            field=models.ImageField(upload_to=spv.models.NegocioImg.generate_folder_for_business),
        ),
    ]
