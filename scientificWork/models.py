#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from moevmCommon.models import UserProfile
from django.utils.encoding import python_2_unicode_compatible
# Описание моделей приложения scientificWork


class Publication(models.Model):
    tpPubl = (
        ('guidelines', 'Методическое указание'),
        ('book', 'Книга'),
        ('journal', 'Статья в журнале'),
        ('compilation', 'Конспект лекции/сборник докладов'),
        ('collection', 'Сборник трудов')
    )
    reIter = (
        ('disposable', 'одноразовый'),
        ('repeating','повторяющийся')
    )
    user =  models.ForeignKey(UserProfile) 
    typePublication = models.CharField("Тип публикации",
                                       max_length="20",
                                       choices=tpPubl,
                                       default="book")
    publishingHouseName = models.CharField("Название издательства", max_length="100", blank=True )  # название издательства
    place = models.CharField("Место издания", max_length="100", blank=True )  #  место издания
    date = models.DateField("Дата издания", null=True, blank=True )  #  дата издания
    volume = models.IntegerField("Объем", null=True, blank=True )  #  объем
    unitVolume = models.CharField("Единицы объёма", max_length="100", blank=True )  #  еденицы объема
    edition = models.IntegerField("Тираж", null=True, blank=True )  #  тираж
    bookName = models.CharField("Название", max_length="300",
                            help_text="Название публикации", blank=True )  #  название публикации
    type = models.CharField("Вид", max_length="100",
                            help_text="Поле заполняется, если тип вашей публикации"
                                      " \"Книга\" или \"Методическое указание\"", blank=True )  #  вид методического издания / книги
    isbn = models.CharField("ISBN", max_length="100",
                            help_text="Поле заполняется, если тип вашей публткации"
                                      "\"Книга\" или \"Методическое указание\"", blank=True )  #  ISBN
    number = models.IntegerField("Номер издания", null=True, blank=True )  #  номер издания
    editor = models.CharField("Редактор сборника", max_length="100", blank=True )  #  редакто сборника
    nameSbornik = models.CharField("Название сборника", max_length="100", blank=True )  #  название сборника
    reiteration = models.CharField("Вид повторения сборника",
                                   choices=reIter,
                                   max_length="10",
                                   default="disposable", 
                                   blank=True 
                                   )  #  вид повторения сборника


class Participation(models.Model):
    tp = (
        ('conference', 'конференция'),
        ('seminar', 'семинар')
    )
    user = models.ForeignKey(UserProfile, default="")
    type = models.CharField("Тип", choices=tp, max_length="10", default="conference")  #  тип: конференция - conference, семинар - seminar
    name = models.CharField("Название", max_length="100")  # название
    date = models.DateField("Дата проведения")  # дата проведения
    place = models.CharField("Место проведения", max_length="100")  # место проведения
    reIter = (
        ('disposable', 'одноразовый'),
        ('repeating', 'повторяющийся')
    )
    reiteration = models.CharField("Вид повторения сборника",
                                    choices=reIter,
                                    max_length="10",
                                    default="disposable"
                                   )  # вид повторения сборника

    rank = models.CharField("Ранг", max_length="100") # ранг


class Rand(models.Model):
    user = models.ForeignKey(UserProfile, default="")
    name = models.CharField("Название НИОКР", max_length="300")  # Название НИОКР
    cipher = models.CharField("Шифр", max_length="300")  #Шифр