#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Подключаем наши модели в админку сайта

# Указываем, что из scientificWork.models импортируем конкретную модель Test_collection
from scientificWork.models import Publication, Participation, Rand
from studentrecords.models import AttendanceRecord, TermProject, TimeTableDay, TimeTableRecord, Project, Grades, Lesson, \
  Lab, Attendance, TimeTable

# Регистрируем импортированную модель в админку
admin.site.register(AttendanceRecord)
admin.site.register(Attendance)
admin.site.register(Lab)
admin.site.register(Lesson)
admin.site.register(Grades)
admin.site.register(Project)
admin.site.register(TermProject)
admin.site.register(TimeTableRecord)
admin.site.register(TimeTableDay)
admin.site.register(TimeTable)