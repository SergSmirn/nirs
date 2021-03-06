# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 23:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_auto_20171125_2311'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Particle',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='energy',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='simulationTime',
        ),
        migrations.AlterField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='doc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logic.Document'),
            preserve_default=False,
        ),
    ]
