# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180524_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('AD', 'System Admin'), ('LA', 'Admin'), ('IN', 'Instructor'), ('TA', 'Teaching Assistant'), ('ST', 'Student')], max_length=2),
        ),
    ]