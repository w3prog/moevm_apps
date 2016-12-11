#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect

def mainPage(request):
  return render(request,"index_main_page.html")