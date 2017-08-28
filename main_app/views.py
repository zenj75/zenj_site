from django.shortcuts import render, render_to_response
import datetime



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
    learns = ['Димитровградский Механико-технологический Колледж Молочной Промышленности',
              'Институт международного права и экономики имени А.С. Грибоедова',
              'Различные курсы (Cisco,Solaris)',
              'Курсы GeekBrains (HTML/CSS, Python1)']
    return render_to_response('school.html', {'learns': learns})

def work_view(request):
    my_works = [{   'name':'Департамент по государственной регистрации прав на недвижимое имущество г.Димитровграда',
                    'prof':'системный администратор',
                    'desc':'обслуживал небольшую сеть организации, сервер Novell Netware'},
                {   'name':'Димитровградский автоагрегатный завод',
                    'prof':'cистемный инженер',
                    'desc':'строил и обслуживал сети с Novell и Linux. миграция с Netware на eDirectory и всё такое'},
                {   'name':'МЕГАФОН (Санкт-Петербург)',
                    'prof':'cистемный инженер',
                    'desc': 'обслуживание и развитие сегмента фиксированной сети оператора, Cisco/Huawei, Linux/Solaris'},
                {   'name':'Северен-Телеком (Санкт-Петербург)',
                    'prof':'системный инженер',
                    'desc':'обслуживание и развитие сети IP/MPLS телеком-оператора'},
                {   'name':'МГТС (Москва)',
                    'prof': 'системный инженер',
                    'desc':'обслуживание и развитие сети IP/MPLS телеком-оператора'}]
    return render_to_response('work.html', {'my_works': my_works})

def base_view(request):
    tel = '+7 (9I6)317 2O-55'
    email = 'zenj75@gmail.com'
    skype = 'ezakharov75'
    return render_to_response('base.html', {'telefon':tel, 'email':email, 'skype':skype})