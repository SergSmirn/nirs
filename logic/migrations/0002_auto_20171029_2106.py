# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 21:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.IntegerField()),
                ('simulationTime', models.IntegerField()),
                ('frequency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Particle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='calculation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Calculation',
        ),
        migrations.AddField(
            model_name='experiment',
            name='particle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logic.Particle'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
