from django.test import TestCase
from django.test.client import Client

client = Client()


class GetPagesTests(TestCase):
    def get_index(self):
        response = client.get("/")

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_students(self):
        response = client.get('/students')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_attendance(self):
        response = client.get('/attendance')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_grades(self):
        response = client.get('/grades')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_group_list(self):
        response = client.get('/group-list')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_timetable(self):
        response = client.get('/timetable')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)

    def get_term_projects(self):
        response = client.get('/term-projects')

        expected = 200
        actual = response.status_code

        self.assertEqual(expected, actual)


class AuthTests(TestCase):
    # тест на авторизацию с правильным логином и паролем
    def test_success(self):
        response = client.post('login', {'username': 'admin', 'password': '123'})
        self.assertRedirects(response, "/", status_code=302, target_status_code=200, msg_prefix='')

    # тест на авторизацию с неправильным логином
    def test_bad_login(self):
        response = client.post('login', {'username': 'admin2', 'password': '123'})
        self.assertEqual(response.content, "Invalid login details supplied.")

    # тест на авторизацию с неправильным паролем
    def test_bad_password(self):
        response = client.post('login/', {'username': 'admin', 'password': '12345'})
        self.assertEqual(response.content, "Invalid login details supplied.")


class DataTests(TestCase):
    def get_students(self):
        pass

    def get_attendance(self):
        pass

    def get_grades(self):
        pass

    def get_group_list(self):
        pass

    def get_timetable(self):
        pass

    def get_term_projects(self):
        pass

