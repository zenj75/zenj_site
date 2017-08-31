# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20170830_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='порядковый номер'),
        ),
    ]
