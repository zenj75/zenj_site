# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(verbose_name='Имя', max_length=32)),
                ('sname', models.CharField(verbose_name='Фамилия', max_length=32)),
                ('mname', models.CharField(verbose_name='Отчество', max_length=32)),
                ('bdate', models.DateField(verbose_name='Дата рождения', max_length=32)),
                ('bplace', models.CharField(verbose_name='Место рождения', max_length=32)),
                ('cur_place', models.CharField(verbose_name='Место проживания', max_length=32)),
                ('email', models.EmailField(verbose_name='Email', blank='True', max_length=32)),
                ('skype', models.CharField(verbose_name='Skype', blank='True', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lname', models.CharField(verbose_name='Учебное заведение', max_length=120)),
                ('course', models.CharField(verbose_name='Курс', max_length=32)),
                ('site', models.CharField(verbose_name='Сайт', blank='True', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wname', models.CharField(verbose_name='Организация', max_length=80)),
                ('prof', models.CharField(verbose_name='Профессия', max_length=32)),
                ('sprof', models.CharField(verbose_name='Доп. профессия', blank='True', max_length=32)),
                ('wdescr', models.TextField(verbose_name='Обязанности')),
                ('site', models.CharField(verbose_name='Сайт', blank='True', max_length=32)),
            ],
        ),
    ]
