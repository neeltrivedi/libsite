# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0008_auto_20160621_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libuser',
            name='model_pic',
            field=models.ImageField(blank=True, default='pic_folder/None/no-img.jpg', null=True, upload_to='libapp/static/pic_folder/'),
        ),
    ]
