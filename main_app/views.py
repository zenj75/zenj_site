from django.shortcuts import render, render_to_response
import datetime
from .models import Work
from .models import School

def main_view(request):
    fname = "Евгений"
    surname = "Николаевич"
    middle_name = "Захаров"
    bdate = datetime.date(1975, 5, 9)
    bplace = 'Димитровград'
    wplace = 'МГТС'
    hplace = 'Москва'
    prof = 'системный инженер'
    dprof = 'преподаватель йоги'
    learn = '<a href="https://geekbrains.ru/" title="GeekBrains">GeekBrains</a>'
    course = 'Django'
    return render_to_response('index.html', {'name':fname, 'surname':surname, 'middle_name':middle_name,
                                             'bdate':bdate, 'bplace':bplace,'wplace':wplace, 'hplace':hplace,
                                             'prof':prof, 'dprof':dprof,'learn':learn,'course':course })

def school_view(request):
    learns = School.objects.all()
    # learns = ['Димитровградский Механико-технологический Колледж Молочной Промышленности',
    #           'Институт международного права и экономики имени А.С. Грибоедова',
    #           'Различные курсы (Cisco,Solaris)',
    #           'Курсы GeekBrains (HTML/CSS, Python1)']
    return render_to_response('school.html', {'learns': learns})

def work_view(request):
    my_works = Work.objects.all()
    return render_to_response('work.html', {'my_works': my_works})

def base_view(request):
    tel = '+7 (9I6)317 2O-55'
    email = 'zenj75@gmail.com'
    skype = 'ezakharov75'
    return render_to_response('base.html', {'telefon':tel, 'email':email, 'skype':skype})

