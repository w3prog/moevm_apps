# -*- coding: utf-8 -*-

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from moevmCommon.models import UserProfile
from .helpers import *


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/studentrecords')
            else:
                return HttpResponse("Your  account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'studentrecords/login.html')


@login_required(login_url="/studentrecords/login")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/studentrecords')


@login_required(login_url="/studentrecords/login")
def attendance(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    attendance_info = []

    if profile.type == 'a' or profile.type == 't' or request.user.is_superuser:
        attendance_info = AttendanceHelper.get_all_attendance()

    if profile.type == 's':
        attendance_info = AttendanceHelper.get_attendance_by_student(profile.id)

    if profile.type == 'h':
        attendance_info = AttendanceHelper.get_attendance_by_group(profile.study_group)

    return render(request, 'studentrecords/attendance.html', {'attendance': attendance_info, 'profile': profile})


@login_required(login_url="/studentrecords/login")
def grades(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    grades_info = []

    if profile.type == 'a' or profile.type == 't' or request.user.is_superuser:
        grades_info = GradesHelper.get_all_grades()

    if profile.type == 'h':
        grades_info = GradesHelper.get_grades_by_group(profile.study_group)

    if profile.type == 's':
        grades_info = GradesHelper.get_grades_by_student(profile.id)

    return render(request, 'studentrecords/grades.html', {'grades': grades_info, 'profile': profile})


@login_required(login_url="/studentrecords/login")
def group_list(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    group_list_info = []

    if profile.type == 'a' or profile.type == 't' or request.user.is_superuser:
        group_list_info = GroupListHelper.get_all_group_lists()

    if profile.type == 'h' or profile.type == 's':
        group_list_info = GroupListHelper.get_this_group_list(profile.study_group)

    return render(request, 'studentrecords/group-list.html', {'grouplist': group_list_info, 'profile': profile})

# def get_report(request):
#     students = UserProfile.objects.filter(role='s')
#     header = "List of the students. Список студентов."
#     pdf = render_to_pdf('students-to-pdf.html', {
#         'article': header,
#         'students': students
#     })
#
#     if pdf:
#         # TODO: Добавить относительный или автогенерирующийся путь
#         pdf_file = open("/home/nick1/mygit/StudentRecords/studentrecords/static/reports/report.pdf", 'w').write(pdf)
#
#     return render(request, 'report-download.html')


@login_required(login_url="/studentrecords/login")
def students(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    students_info = []

    if profile.type == 'a' or request.user.is_superuser:
        students_info = UserProfile.objects.filter(type='s')

    return render(request, 'studentrecords/students.html', {'students': students_info, 'profile': profile})


@login_required(login_url="/studentrecords/login")
def term_projects(request):

    profile = UserProfile.get_profile_by_user_id(request.user.id)

    term_projects_info = []

    if profile.type == 'a' or profile.type == 't' or request.user.is_superuser:
        term_projects_info = TermProjectsHelper.get_all_term_projects()

    if profile.type == 'h' or profile.type == 's':
        term_projects_info = TermProjectsHelper.get_group_term_projects(profile.study_group)

    return render(request, 'studentrecords/term-projects.html', {'projectlist': term_projects_info, 'profile': profile})


@login_required(login_url="/studentrecords/login")
def timetable(request):
    return render(request, 'studentrecords/timetable.html', {})
