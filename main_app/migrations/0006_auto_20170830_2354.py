# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_person_sprof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='course',
            field=models.CharField(verbose_name='Факультет/Курс', max_length=32),
        ),
    ]
