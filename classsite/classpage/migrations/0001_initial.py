# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-25 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlemax', models.CharField(max_length=30)),
                ('titlemin', models.CharField(max_length=40)),
                ('introduction', models.CharField(max_length=150)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('photot', models.ImageField(upload_to='')),
            ],
        ),
    ]
