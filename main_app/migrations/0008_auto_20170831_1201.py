# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_school_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='site',
            field=models.CharField(blank='True', default='', max_length=32, verbose_name='Сайт'),
        ),
    ]
