# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_work_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='wyear',
            field=models.PositiveIntegerField(verbose_name='Период работы работы', default=1),
        ),
    ]
