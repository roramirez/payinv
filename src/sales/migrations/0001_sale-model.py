# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-17 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_datetime-model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('internal_id', models.CharField(max_length=100)),
                ('total_value', models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Total Value')),
                ('done_at', models.DateField()),
                ('concept', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]