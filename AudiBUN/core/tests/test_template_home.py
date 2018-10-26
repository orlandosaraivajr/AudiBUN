from django.test import TestCase, Client
from django.shortcuts import resolve_url as r
from AudiBUN.empresas.form import EmpresaForm
from django.contrib.auth.models import User

class HomeTemplateTest(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password)
        self.client.login(username=self.username,
                          password=self.password)
        self.resp = self.client.get(r('home'))

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exit_link(self):
        self.assertContains(self.resp, 'href="/logout')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)


class IndexTemplateTest(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password)
        self.client.login(username=self.username,
                          password=self.password)
        self.resp = self.client.get(r('index'))

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exit_link(self):
        self.assertContains(self.resp, 'href="/logout')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)
