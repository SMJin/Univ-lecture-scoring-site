from django.shortcuts import render
from .models import Lectures_info

def index(request):
    lecture_i = Lectures_info.objects
    context = {'lecture': lecture_i}
    return render(request, 'index.html', context)

def lecture_test(request):
    lecture_i = Lectures_info.objects
    context = {'lecture': lecture_i}
    return render(request, 'show_lecture_test.html', context)