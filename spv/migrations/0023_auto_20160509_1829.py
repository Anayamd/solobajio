# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spv', '0022_auto_20160331_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.AlterModelOptions(
            name='industry',
            options={'verbose_name': 'Industry', 'verbose_name_plural': 'Industries'},
        ),
        migrations.AlterField(
            model_name='openinghour',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='spv.Negocio'),
        ),
    ]
