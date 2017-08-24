from django.shortcuts import render, render_to_response

def main_view(request):
    return render_to_response('index.html')

def school_view(request):
    return render_to_response('school.html')

def work_view(request):
    return render_to_response('work.html')

