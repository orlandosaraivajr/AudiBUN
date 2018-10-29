from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.shortcuts import resolve_url as r

class HomeGetRedirectTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_302_response(self):
        self.assertEqual(302, self.resp.status_code)

class LoginTemplateGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('login'))

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('<form', 1),
            ('</form>', 1),
            ('Fatec Araras', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class LoginPostTest(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password)
        data = {}
        data['username'] = self.username
        data['password'] = self.password
        self.resp = self.client.post(r('login'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)


class LoginPostTestFail(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = '123mudar'
        self.client = Client()
        User.objects.create_user(
            self.username,
            'admin@admin.com',
            self.password)
        data = {}
        data['username'] = 'usuario_errado'
        data['password'] = 'senha_errada'
        self.resp = self.client.post(r('login'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('btn-danger', 1),
            ('Acesso Negado', 1),
            ('Fatec Araras', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
