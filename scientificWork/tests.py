# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from scientificWork.models import *
from django.test.client import Client
from django.contrib.auth.models import User
from scientificWork.models import Publication, UserProfile, Rand, Participation

c = Client()

# Тесты авторизации
class AuthorizationTest(TestCase):
    def setUp(self):
        # Создаем активного пользователя
        self.username = 'admin'
        self.password = 'secret'
        self.user = User.objects.create_user(self.username,
        'mail@example.com',
        self.password)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        # Создаем неактивного пользователя
        self.username2 = 'adminBloked'
        self.user2 = User.objects.create_user(self.username2,
        'mail@example.com',
        self.password)
        self.user2.is_staff = True
        self.user2.is_superuser = True
        self.user2.is_active = False
        self.user2.save()

    # тест на авторизацию с правильным логином и паролем
    def test_success(self):
        response = c.post('/scientificWork/login/', {'username': 'admin', 'password': 'secret'})
        self.assertRedirects(response, "/scientificWork/", status_code=302, target_status_code=200, msg_prefix='')

    # тест на авторизацию с неправильным логином
    def test_bad_login(self):
        response = c.post('/scientificWork/login/', {'username': 'admin2', 'password': 'secret'})
        self.assertEqual(response.content, "Invalid login details supplied.")

    # тест на авторизацию с неправильным паролем
    def test_bad_password(self):
        response = c.post('/scientificWork/login/', {'username': 'admin', 'password': 'secret1'})
        self.assertEqual(response.content, "Invalid login details supplied.")

    # тест на авторизацию неактивного пользователя
    def test_inactive_user(self):
        response = c.post('/scientificWork/login/', {'username': 'adminBloked', 'password': 'secret'})
        self.assertEqual(response.content, "Your  account is disabled.")


# Тесты на получение страниц
class GetPagesTest(TestCase):
	# тест получения главной страницы
    def test_home_page(self):
        response = c.get('/scientificWork/')
        self.assertEqual(response.status_code, 200)

    # тест получения страницы Участие в конференциях/семинарах
    def test_competitions_page(self):
        response = c.get('/scientificWork/competitions')
        self.assertEqual(response.status_code, 200)

    # тест получения страницы Публикации
    def test_publications_page(self):
        response = c.get('/scientificWork/publications')
        self.assertEqual(response.status_code, 200)

    # тест получения страницы НИОКР
    def test_rads_page(self):
        response = c.get('/scientificWork/rads')
        self.assertEqual(response.status_code, 200)

# Тесты на фильтрацию
class FilterPagesTest(TestCase):
	fixtures = ['data.json']

# Публикации:
	# тест на получение всех публикации
	def test_publication_all(self):
		response = c.get('/scientificWork/publications')
		self.assertEqual(response.context['notes'].__len__(), 3)

	# тест на получение публикаций с типом Книга
	def test_publication_onlyBook(self):
		response = c.get('/scientificWork/publications?userName=&typePublication=book&publishingHouseName=&place=&date=&volume=&unitVolume=&edition=&bookName=&type=&isbn=&number=&editor=&nameSbornik=&reiteration=&button_filter=')
		self.assertEqual(response.context['notes'].__len__(), 1)

	# тест на получение публикаций с типом Статья в журнале
	def test_publication_onlyStiteInJournal(self):
		response = c.get('/scientificWork/publications?userName=&typePublication=journal&publishingHouseName=&place=&date=&volume=&unitVolume=&edition=&bookName=&type=&isbn=&number=&editor=&nameSbornik=&reiteration=&button_filter=')
		self.assertEqual(response.context['notes'].__len__(), 0)

# Конкурсы и семинары
	# тест на получение всех конкурсов и семинаров
	def test_competitions_all(self):
		response = c.get('/scientificWork/competitions')
		self.assertEqual(response.context['comps'].__len__(), 3)

	# тест на получение повторяющихся конкурсов и семинаров
	def test_competitions_onlyBook(self):
		response = c.get('/scientificWork/competitions?userName=&type=&name=&place=&date=&rank=&reiteration=repeating&button_filter=')
		self.assertEqual(response.context['comps'].__len__(), 3)

	# тест на получение конкурсов и семинаров с названием "авып"
	def test_competitions_onlyStiteInJournal(self):
		response = c.get('/scientificWork/competitions?userName=&type=&name=авып&place=&date=&rank=&reiteration=&button_filter=')
		self.assertEqual(response.context['comps'].__len__(), 0)

# НИОКР
	# тест на получение всех НИОКР
	def test_rands_all(self):
		response = c.get('/scientificWork/rads')
		self.assertEqual(response.context['rands'].__len__(), 3)

	# тест на получение всех НИОКР на фамилию Столетов
	def test_rands_onlyStoletov(self):
		response = c.get('/scientificWork/rads?userName=Столетов&name=&cipher=&button_filter=')
		self.assertEqual(response.context['rands'].__len__(), 1)

	# тест на получение всех НИОКР на шифр "62784"
	def test_rands_onlyChihper62784(self):
		response = c.get('/scientificWork/rads?userName=&name=&cipher=62784&button_filter=')
		self.assertEqual(response.context['rands'].__len__(), 0)

# Отчёт о численности
	# количество аспирантов
	def test_strength_aspirant(self):
		response = c.get('/scientificWork/strength')
		self.assertEqual(response.context['aspirant'], 0)

	# количество докторантов
	def test_strength_doctorant(self):
		response = c.get('/scientificWork/strength')
		self.assertEqual(response.context['doctorant'], 2)

	def test_strength_soiskatel(self):
		response = c.get('/scientificWork/strength')
		self.assertEqual(response.context['soiskatel'], 2)

	# количество стажеров
	def test_strength_stajer(self):
		response = c.get('/scientificWork/strength')
		self.assertEqual(response.context['stajer'], 0)