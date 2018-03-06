# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20171219_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16, unique=True)),
                ('u_password', models.CharField(max_length=33)),
                ('u_icon', models.ImageField(upload_to='uploadfiles')),
                ('u_email', models.CharField(max_length=50)),
                ('u_phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
