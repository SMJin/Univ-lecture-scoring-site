from django.contrib import admin
from mainLecture.models import Lectures_info
from mainLecture.models import Professor_info
from mainLecture.models import Show_lectures_in_comment

admin.site.register(Lectures_info)
admin.site.register(Professor_info)
admin.site.register(Show_lectures_in_comment)