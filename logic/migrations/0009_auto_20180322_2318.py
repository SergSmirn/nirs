# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 23:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0008_experiment_param'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_data', models.TextField()),
                ('supply_voltage', models.FloatField()),
                ('resistance', models.FloatField(default=15000.0)),
                ('capacitance', models.FloatField(default=1e-15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(choices=[('point', 'Точечная модель'), ('voltage', 'Модель напряжений')], max_length=50)),
                ('sim_type', models.CharField(choices=[('monte_carlo', 'Монте-Карло'), ('analytical', 'Аналитический')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Experiment',
        ),
    ]
