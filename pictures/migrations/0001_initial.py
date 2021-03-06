# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-06 09:41
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(max_length=30)),
                ('imageDescription', models.CharField(max_length=30)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('imageCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='imageLocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Location'),
        ),
    ]
