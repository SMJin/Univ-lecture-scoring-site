from django.shortcuts import render, get_object_or_404
from .models import Lectures_info

def index(request):
    lecture_i = Lectures_info.objects
    context = {'lecture': lecture_i}
    return render(request, 'index.html', context)

def lecture_test(request, lecture_id):
    lecture_more = get_object_or_404(Lectures_info, pk = lecture_id)
    # lecture_i = Lectures_info.objects
    context = {'lecture': lecture_more}
    return render(request, 'show_lecture_test.html', context)