# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='textResumo',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
