# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-25 23:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import logic.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0005_auto_20171125_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=logic.models.user_directory_path),
        ),
    ]
