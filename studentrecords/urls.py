from django.conf.urls import url
from views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^(index(.html)?)?$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^attendance', attendance, name='attendance'),
    url(r'^grades', grades, name='grades'),
    url(r'^group-list', group_list, name='group-list'),
    url(r'^timetable', timetable, name='timetable'),
    url(r'^students', students, name='students'),
    url(r'^term-projects', term_projects, name='term-projects'),
    url(r'^login', user_login, name='login'),
    url(r'^logout', user_logout, name='logout'),
    # url(r'^report', get_report, name='get-report')
]
