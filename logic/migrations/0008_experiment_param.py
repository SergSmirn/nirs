# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0007_auto_20171127_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='param',
            field=models.IntegerField(default=0),
        ),
    ]
