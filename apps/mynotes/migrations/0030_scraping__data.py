# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-26 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0029_scraping'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraping',
            name='_data',
            field=models.TextField(blank=True, db_column='data'),
        ),
    ]
