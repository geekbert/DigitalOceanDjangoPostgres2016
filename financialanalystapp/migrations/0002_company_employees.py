# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financialanalystapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Employees',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
