# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20170831_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='tel',
            field=models.CharField(default='', max_length=9, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='site',
            field=models.CharField(default='.', max_length=32, verbose_name='Сайт'),
        ),
    ]
