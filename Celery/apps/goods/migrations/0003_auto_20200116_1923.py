# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200116_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='商品详情'),
        ),
    ]
