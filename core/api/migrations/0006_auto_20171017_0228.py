# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 02:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170913_0258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='spec_pop_score',
            new_name='specpop_score',
        ),
    ]