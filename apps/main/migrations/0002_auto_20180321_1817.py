# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-21 18:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
