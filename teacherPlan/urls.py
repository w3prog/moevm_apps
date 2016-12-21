#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf.urls import url, include
from django.contrib.contenttypes import views as contenttype_views
from views import *

urlpatterns = patterns(
   '',
   url(r'^$', index, name='tpindex'),

   #auth
   url(r'^login$', loginTeacher, name='tplogin', ),
   url(r'^loginwitherror$', errorLoginTeacher, name='tploginwitherror', ),
   url(r'^logout$', logoutTeacher, name='tplogout', ),

   #plans
   url(r'^listOfPlans$', listOfPlans, name='tpplanlist', ),
   url(r'^plan/(?P<id>[0-9a-z]+)$', plan, name='tpplan', ),
   url(r'^currentPlan/', currentPlan, name='currentPlan', ),
   url(r'^registerTeacher/', registerTeacher,name='registerTeacher' ),

   #forms
   url(r'^studybookList/(?P<id>[0-9a-z]+)', studybookList, name='studybookList'),
   url(r'^disciplineList/(?P<id>[0-9a-z]+)', disciplineList, name='disciplineList'),
   url(r'^scWorkList/(?P<id>[0-9a-z]+)', scWorkList, name='scWorkList'),
   url(r'^participationList/(?P<id>[0-9a-z]+)', participationList, name='participationList'),
   url(r'^publicationList/(?P<id>[0-9a-z]+)', publicationList, name='publicationList'),
   url(r'^qualificationList/(?P<id>[0-9a-z]+)', qualificationList, name='qualificationList'),
   url(r'^difWorkList/(?P<id>[0-9a-z]+)', difWorkList, name='difWorkList'),

   url(r'^pdf/(?P<id>[0-9a-z]+)', makePDF, name='pdf'),
)