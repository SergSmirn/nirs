# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-07 16:23
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0011_simulationresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='experiment_data',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=3),
        ),
        migrations.AlterField(
            model_name='simulationresult',
            name='let_and_cross_section',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=2),
        ),
    ]
