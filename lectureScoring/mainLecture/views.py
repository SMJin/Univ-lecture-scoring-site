from django.shortcuts import render
from .models import Lectures_info

def index(request):
    return render(request, 'index.html')

def lecture_test(request):
    lectur_i = Lectures_info.objects.all()
    context = {'lecture': lectur_i}
    return render(request, 'show_lecture_test.html', context)