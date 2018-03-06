# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foottypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=20)),
                ('childtypenames', models.CharField(max_length=20)),
                ('typesort', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=20)),
                ('productid1', models.CharField(max_length=100)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=20)),
                ('marketprice1', models.CharField(max_length=20)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=20)),
                ('productid2', models.CharField(max_length=100)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=20)),
                ('marketprice2', models.CharField(max_length=20)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=20)),
                ('productid3', models.CharField(max_length=100)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=20)),
                ('marketprice3', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axfMainshow',
            },
        ),
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axfMustbuy',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axfNav',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axfShop',
            },
        ),
    ]