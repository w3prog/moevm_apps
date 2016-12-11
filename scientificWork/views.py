#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from scientificWork.models import Publication, Rand, Participation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from datetime import datetime
from moevmCommon.models import UserProfile


# Константы
MAX_ELEMENT_PAGE = 3; # Максимальное количество элементов на странице

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def index(request):
	return render(request,'scientificWork/index.html')


def competitions(request):
    comp_list = Participation.objects.all()
    users = UserProfile.objects.all()
    users_with_names = User.objects.all()
    userName = ''
    t=''
    n = ''
    dt = ''
    p = ''    
    r=''
    rk='' 
    if request.GET:
        userName = request.GET.get('userName')
        t=request.GET.get('type')
        n = request.GET.get('name')
        p = request.GET.get('place')
        dt = request.GET.get('date')        
        r = request.GET.get('reiteration')
        rk = request.GET.get('rank')  
        if (userName != ''): 
            userNameList = userName.split()
            users_with_names = users_with_names.filter(last_name__icontains=userNameList[0])
            if len(userNameList) > 1: users_with_names = users_with_names.filter(first_name__icontains=userNameList[1])

            if users_with_names:
                A = []
                for item in users_with_names:
                    users = UserProfile.objects.all()
                    users = users.filter(user_id=item.id)
                    if len(userNameList) > 2: 
                        users = users.filter(patronymic__icontains=userNameList[2])
                    if users.count() > 0:
                        A.append(users[0].id)
                #user_ids = users_with_names[0].id
                comp_list = comp_list.filter(user_id__in=A)
        if (t != ''): comp_list = comp_list.filter(type=t)
        if (n != ''): comp_list = comp_list.filter(name=n)
        if (p != ''): comp_list = comp_list.filter(place=p)
        if (dt != ''):
            datetime_objects = dt.split("-")
            if len(datetime_objects) == 1:
                if isint(dt):
                    comp_list = comp_list.filter(date__year=int(dt))
                else:
                    comp_list = comp_list.filter(type='sdafsdfasdf');
            else:
                datetime_objects = datetime.strptime(dt, '%d-%M-%Y').strftime('%Y-%M-%d')
                comp_list = comp_list.filter(date=datetime_objects)
        if (r != ''): comp_list = comp_list.filter(reiteration=r)        
        if (rk != ''): comp_list = comp_list.filter(rank=rk)       
    if 'button_reset' in request.GET:
        comp_list=Participation.objects.all()
    paginator = Paginator(comp_list, MAX_ELEMENT_PAGE)
    page = request.GET.get('page')
    try:
        comp_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comp_list = paginator.page(1)
    except EmptyPage:
        comp_list = paginator.page(paginator.num_pages)
    return render(request, 'scientificWork/competitions.html',
                      {'comps': comp_list,
                       't': t,
                       'p': p,
                       'n': n,
                       'dt': dt,
                       'rk': rk,
                       'r': r,
                       'userName': userName,
                       })
    

def publications(request):
    s = Publication.objects.all()
    users_with_names = User.objects.all()
    userName = ''
    pH = ''
    pl = ''
    tp = ''
    dt = ''
    vl = ''
    uvl = ''
    ed = ''
    nm = ''
    type = ''
    ISBN = ''
    number = ''
    editor = ''
    nameSbornik = ''
    reiteration = ''
    if request.GET:
        userName = request.GET.get('userName')
        pH = request.GET.get('publishingHouseName')
        pl = request.GET.get('place')
        tp = request.GET.get('typePublication')
        dt = request.GET.get('date')
        vl = request.GET.get('volume')
        uvl = request.GET.get('unitVolume')
        ed = request.GET.get('edition')
        nm = request.GET.get('bookName')
        type = request.GET.get('type')
        ISBN = request.GET.get('isbn')
        number = request.GET.get('number')
        editor = request.GET.get('editor')
        nameSbornik = request.GET.get('nameSbornik')
        reiteration = request.GET.get('reiteration')
        if (userName != ''): 
            userNameList = userName.split()
            users_with_names = users_with_names.filter(last_name__icontains=userNameList[0])
            if len(userNameList) > 1: users_with_names = users_with_names.filter(first_name__icontains=userNameList[1])

            if users_with_names:
                A = []
                for item in users_with_names:
                    users = UserProfile.objects.all()
                    users = users.filter(user_id=item.id)
                    if len(userNameList) > 2: 
                        users = users.filter(patronymic__icontains=userNameList[2])
                    if users.count() > 0:
                        A.append(users[0].id)
                #user_ids = users_with_names[0].id
                s = s.filter(user_id__in=A)
        if (pH != ''): s = s.filter(publishingHouseName=pH)
        if (pl != ''): s = s.filter(place=pl)
        if (tp != ''): s = s.filter(typePublication=tp)
        if (dt != ''):
            datetime_objects = dt.split("-")
            if len(datetime_objects) == 1:
                if isint(dt):
                    s = s.filter(date__year=int(dt))
                else:
                    s = s.filter(type='-23534fdsg')
            else:
                datetime_objects = datetime.strptime(dt, '%d-%M-%Y').strftime('%Y-%M-%d')
                s = s.filter(date=datetime_objects)
        if (vl != ''): s = s.filter(volume=vl)
        if (uvl != ''): s = s.filter(unitVolume=uvl)
        if (ed != ''): s = s.filter(edition=ed)
        if (nm != ''): s = s.filter(bookName=nm)
        if (type != ''): s = s.filter(type=type)
        if (ISBN != ''): s = s.filter(isbn=ISBN)
        if (number != ''): s = s.filter(number=number)
        if (editor != ''): s = s.filter(editor=editor)
        if (nameSbornik != ''): s = s.filter(nameSbornik=nameSbornik)
        if (reiteration != ''): s = s.filter(reiteration=reiteration)
    if 'button_reset' in request.GET:
        s = Publication.objects.all()
    paginator = Paginator(s, MAX_ELEMENT_PAGE)
    page = request.GET.get('page')
    try:
        s = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        s = paginator.page(1)
    except EmptyPage:
        s = paginator.page(paginator.num_pages)
    return render(request, 'scientificWork/publications.html',
                  {'notes': s,
                   'userName': userName,
                   'pH': pH,
                   'pl': pl,
                   'tp': tp,
                   'dt': dt,
                   'vl': vl,
                   'uvl': uvl,
                   'ed': ed,
                   'nm': nm,
                   'type': type,
                   'ISBN': ISBN,
                   'number': number,
                   'editor': editor,
                   'nameSbornik': nameSbornik,
                   'reiteration': reiteration
                   })

def rads(request):
    rand_list=Rand.objects.all()
    users = UserProfile.objects.all()
    users_with_names = User.objects.all()
    userName = ''
    n=''
    c=''
    if request.GET:
        userName = request.GET.get('userName')
        n=request.GET.get('name')
        c=request.GET.get('cipher')
        if(n!=''):rand_list=rand_list.filter(name=n)
        if(c!=''):rand_list=rand_list.filter(cipher=c)
        if (userName != ''): 
            userNameList = userName.split(" ")
            users_with_names = users_with_names.filter(last_name__icontains=userNameList[0])
            if len(userNameList) > 1: users_with_names = users_with_names.filter(first_name__icontains=userNameList[1])

            if users_with_names:
                A = []
                for item in users_with_names:
                    users = UserProfile.objects.all()
                    users = users.filter(user_id=item.id)
                    if len(userNameList) > 2: 
                        users = users.filter(patronymic__icontains=userNameList[2])
                    if users.count() > 0:
                        A.append(users[0].id)
                rand_list = rand_list.filter(user_id__in=A)
    if 'button_reset' in request.GET:
        rand_list=Rand.objects.all()
    paginator=Paginator(rand_list,MAX_ELEMENT_PAGE)
    page=request.GET.get('page')
    try:
        rand_list=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rand_list=paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rands=paginator.page(paginator.num_pages)

    return render(request,'scientificWork/rads.html',{"rands": rand_list,'n':n,'c':c, 'userName': userName,})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/scientificWork/')
            else:
                return HttpResponse("Your  account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'scientificWork/login.html', {})


# Используйте декоратор login_required(), чтобы гарантировать, что только авторизированные пользователи смогут получить доступ к этому представлению.
@login_required
def user_logout(request):
    # Поскольку мы знаем, что только вошедшие в систему пользователи имеют доступ к этому представлению, можно осуществить выход из системы
    logout(request)
    return HttpResponseRedirect('/scientificWork/')

def strength(request):
    aspirant = UserProfile.objects.filter(academic_state='a').count();
    doctorant = UserProfile.objects.filter(academic_state='d').count();
    soiskatel = UserProfile.objects.filter(academic_state='s').count();
    stajer = UserProfile.objects.filter(academic_state='st').count();
    return render(request,'scientificWork/strength.html', {
        'aspirant' : aspirant,
        'doctorant' : doctorant,
        'soiskatel' : soiskatel,
        'stajer' : stajer
        })