# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0018_auto_20180408_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='geometry',
            field=models.CharField(choices=[('disc', 'Диск'), ('sphere', 'Сфера')], max_length=15),
        ),
    ]
