from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def lecture_test(request):
    return render(request, 'show_lecture_test.html')