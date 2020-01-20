# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.SmallIntegerField(verbose_name='状态')),
                ('detail', tinymce.models.HTMLField(verbose_name='状态详情')),
            ],
            options={
                'db_table': 'test_dable',
            },
        ),
    ]
