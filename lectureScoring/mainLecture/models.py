from django.db import models

# Create your models here.
class Lectures_info(models.Model):
    lecture_title = models.CharField(max_length=50)
    lecture_professor_name = models.CharField(max_length=10)
    university_name = models.CharField(max_length=10)
    semester = models.CharField(max_length=50)
    lecture_scoring = models.CharField(max_length=50)
    number_of_tests = models.CharField(max_length=50)
    meeting = models.CharField(max_length=50)


class Professor_info(models.Model):
    professor_name = models.CharField(max_length=50)
    professor_educational_background = models.CharField(max_length=50)
    professor_spec = models.CharField(max_length=50)


class Show_lectures_in_comment(models.Model):
    lecture_title = models.CharField(max_length=50)
    professor_name = models.CharField(max_length=50)
    lecture_scoring = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
