from django.shortcuts import render, render_to_response

def main_view(request):
    return render_to_response('index.html')

def school_view(request):
    learns = ['Димитровградский Механико-технологический Колледж Молочной Промышленности',
              'Институт международного права и экономики имени А.С. Грибоедова', 'различные курсы Cisco и Solaris']
    return render_to_response('school.html', {'learns': learns} )

def work_view(request):
    my_works = ['Департамент по государственной регистрации прав на недвижимое имущество г.Димитровграда',
             'Димитровградский автоагрегатный завод', 'МЕГАФОН (Санкт-Петербург)', 'Северен-Телеком (Санкт-Петербург)',
             'МГТС (Москва)']
    return render_to_response('work.html', {'my_works':my_works} )


