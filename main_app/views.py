from django.shortcuts import render, render_to_response
from .models import Work
from .models import School
from .models import Person

def main_view(request):
    learn = '<a href="https://geekbrains.ru/" title="GeekBrains">GeekBrains</a>'
    pl = Person.objects.all()
    return render_to_response('index.html', {'pers':pl,'learn':learn })

def school_view(request):
    learns = School.objects.all()
    pl = Person.objects.all()
    return render_to_response('school.html', {'learns': learns,'pers':pl})

def work_view(request):
    my_works = Work.objects.all()
    pl = Person.objects.all()
    return render_to_response('work.html', {'my_works': my_works,'pers':pl})


