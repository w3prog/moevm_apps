# -*- coding: utf-8 -*-

from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
from moevmCommon.models import UserProfile


class AttendanceRecord(models.Model):
    lesson_name = models.CharField(max_length=30)
    date = models.DateTimeField()

    class Meta:
        db_table = 'attendancerecord'


class Attendance(models.Model):
    user = models.ForeignKey(UserProfile)
    attendance_records = ListField(EmbeddedModelField(AttendanceRecord))

    class Meta:
        db_table = 'attendance'


class Lab(models.Model):
    title = models.CharField(max_length=50)
    grade = models.IntegerField()

    class Meta:
        db_table = 'lab'


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    labs = ListField(EmbeddedModelField(Lab))

    class Meta:
        db_table = 'lesson'


class Grades(models.Model):
    user = models.ForeignKey(UserProfile)
    grades = ListField(EmbeddedModelField(Lesson))

    class Meta:
        db_table = 'grades'


class Project(models.Model):
    lesson_name = models.CharField(max_length=30)
    project_title = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)

    class Meta:
        db_table = 'projects'


class TermProject(models.Model):
    user = models.ForeignKey(UserProfile)
    projects = ListField(EmbeddedModelField(Project))

    class Meta:
        db_table = 'termprojects'


class TimeTableRecord(models.Model):
    order_number = models.IntegerField(default=1)
    lesson_name = models.CharField(max_length=50)


class TimeTableDay(models.Model):
    day_of_week = models.IntegerField(default=1)
    is_first_week = models.BooleanField()
    records = ListField(EmbeddedModelField(TimeTableRecord))


class TimeTable(models.Model):
    group = models.CharField(max_length=30)
    timetable = ListField(EmbeddedModelField(TimeTableDay))

    class Meta:
        db_table = 'timetable'


__all__ = ['TimeTable', 'Attendance', 'Grades', 'TermProject']
