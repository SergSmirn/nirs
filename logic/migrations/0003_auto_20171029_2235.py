# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_auto_20171029_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='energy',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='frequency',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='simulationTime',
            field=models.FloatField(default=0),
        ),
    ]