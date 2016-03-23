# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0002_negocio_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='mentions',
            field=models.SmallIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='negocio',
            name='cel1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cel1', to='spv.PhoneModel'),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='cel2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cel2', to='spv.PhoneModel'),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='cel3',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cel3', to='spv.PhoneModel'),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='social_fb',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='social_website',
            field=models.URLField(blank=True),
        ),
    ]
