from django.db import models

# Create your models here.

class Work(models.Model):
    order = models.PositiveIntegerField(verbose_name='порядковый номер',default=0);
    wname = models.CharField(verbose_name='Организация',max_length=80);
    prof = models.CharField(verbose_name='Профессия',max_length=32);
    # sprof = models.CharField(verbose_name='Доп. профессия',max_length=32,blank='True');
    wdescr = models.TextField(verbose_name='Обязанности');
    site = models.CharField(verbose_name='Сайт',blank='True',max_length=32);
    wyear = models.PositiveIntegerField(verbose_name='Период работы работы',default=1);

    def __str__(self):
        return self.wname;

class Person(models.Model):
    fname = models.CharField(verbose_name='Имя',max_length=32);
    sname = models.CharField(verbose_name='Фамилия',max_length=32);
    mname = models.CharField(verbose_name='Отчество',max_length=32);
    bdate = models.DateField(verbose_name='Дата рождения',max_length=32);
    bplace = models.CharField(verbose_name='Место рождения',max_length=32);
    cur_place = models.CharField(verbose_name='Место проживания',max_length=32);
    email = models.EmailField(verbose_name='Email',blank='True',max_length=32);
    skype = models.CharField(verbose_name='Skype',blank='True',max_length=32);
    sprof = models.CharField(verbose_name='Доп. профессия',max_length=32,blank='True');

    def __str__(self):
        return self.fname;

class School(models.Model):
    lname = models.CharField(verbose_name='Учебное заведение',max_length=120);
    course = models.CharField(verbose_name='Факультет/Курс',max_length=32);
    site = models.CharField(verbose_name='Сайт',blank='True',max_length=32);

    def __str__(self):
        return self.lname;
