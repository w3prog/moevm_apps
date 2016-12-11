#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Подключаем наши модели в админку сайта

# Указываем, что из scientificWork.models импортируем конкретную модель Test_collection
from scientificWork.models import Publication, Participation, Rand
# Регистрируем импортированную модель в админку
admin.site.register(Publication)
admin.site.register(Rand)
admin.site.register(Participation)