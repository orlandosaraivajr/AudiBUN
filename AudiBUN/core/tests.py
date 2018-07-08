from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_exit_link(self):
        self.assertContains(self.resp, 'href="/login')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)

class LoginTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/login/')

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'login.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_login_link(self):
        self.assertContains(self.resp, 'href="/index')