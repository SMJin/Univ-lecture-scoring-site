from django.shortcuts import render, get_object_or_404
from .models import Lectures_info, Professor_info

def index(request):
    lecture_i = Lectures_info.objects
    context = {'lecture': lecture_i}
    return render(request, 'index.html', context)

def lecture_test(request, lecture_id):
    lecture_more = get_object_or_404(Lectures_info, pk = lecture_id)
    professor_info = Professor_info.objects
    # lecture_i = Lectures_info.objects
    context = {'lecture': lecture_more, 'professor': professor_info}
    return render(request, 'show_lecture_test.html', context)

def lecture(request):
    return render(request, 'show_lecture.html')