from .models import *
from moevmCommon.models import UserProfile


class GradesHelper:
    @staticmethod
    def get_grades_by_student(student_id):
        return Grades.objects.filter(user_id=student_id)

    @staticmethod
    def get_all_grades():
        return Grades.objects.all()

    @staticmethod
    def get_grades_by_group(study_group):
        all_grades = Grades.objects.all()

        return list(filter(lambda x: x.study_group == study_group, all_grades))


class AttendanceHelper:
    @staticmethod
    def get_attendance_by_student(student_id):
        return Attendance.objects.filter(user_id=student_id)

    @staticmethod
    def get_all_attendance():
        return Attendance.objects.all()

    @staticmethod
    def get_attendance_by_group(study_group):
        all_attendance = Attendance.objects.all()

        return list(filter(lambda x: x.study_group == study_group, all_attendance))


class GroupListHelper:
    @staticmethod
    def get_all_group_lists():
        students = UserProfile.objects.filter(type='s')

        group_list = {}

        for student in students:
            group = student.study_group
            if group not in group_list:
                group_list[group] = []

            group_list[group].append(student)

        return group_list

    @staticmethod
    def get_this_group_list(study_group):
        return GroupListHelper.get_all_group_lists()[study_group]


class TimetableHelper:
    @staticmethod
    def get_all_groups_timetable():
        pass

    @staticmethod
    def get_group_timetable(study_group):
        pass


class TermProjectsHelper:
    @staticmethod
    def get_all_term_projects():
        projects = TermProject.objects.all()

        project_list = {}

        for project in projects:
            group = project.user.study_group
            if group not in project_list:
                project_list[group] = []

            project_list[group].append(project)

        return project_list

    @staticmethod
    def get_group_term_projects(study_group):
        pass


__all__ = ['GradesHelper', 'AttendanceHelper', 'GroupListHelper', 'TimetableHelper', 'TermProjectsHelper']
