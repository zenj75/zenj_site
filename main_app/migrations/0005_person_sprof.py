# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_work_wyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sprof',
            field=models.CharField(verbose_name='Доп. профессия', max_length=32, blank='True'),
        ),
    ]
