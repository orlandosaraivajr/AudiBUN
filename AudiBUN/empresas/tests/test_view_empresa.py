from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.shortcuts import resolve_url as r
from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


class cadastroEmpresaGet(TestCase):
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
        self.resp = self.client.get(r('empresas:empresas_cadastrar'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas_cadastro.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('RC', 2),
            ('Quadra', 1),
            ('Fone', 1),
            ('Empresa', 11),
            ('CNPJ', 1),
            ('Atividade', 1),
            ('Responsável', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 15),
            ('type="text"', 12),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)


class cadastroEmpresaPostValid(TestCase):
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
        data = {}
        data['ref_cad'] = "12.5.12.01.001"
        data['area_lote']  = "50 metros",
        data['area_construida'] = "50 metros",
        data['name'] = "INDUSTRIA STARK LTDA"
        data['cnpj'] = "62.823.257/0001-09"
        data['categoria_atividade'] = "prestacao"
        data['atividade'] = "ATIVIDADE MILITAR"
        data['endereco'] = "RUA SHIELD, 199"
        data['quadra'] = "10"
        data['lote'] = "2"
        data['categoria_distrito'] = "0"
        data['email'] = "tony@stark.com"
        data['phone'] = "055-19-3541-0000"
        data['responsavel'] = "Anotny Stark"
        data['observacao'] = "1"
        self.resp = self.client.post(r('empresas:empresas_cadastrar'), data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_save_Empresa(self):
        self.assertTrue(EmpresaModel.objects.exists())


class cadastroEmpresaPostInvalid(TestCase):
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
        data = {}
        data['ref_cad'] = "12.5.12.01.001"
        data['name'] = "INDUSTRIA STARK LTDA"
        data['atividade'] = "ATIVIDADE MILITAR"
        data['endereco'] = "RUA SHIELD, 199"
        data['quadra'] = "10"
        data['lote'] = "2"
        self.resp = self.client.post(r('empresas:empresas_cadastrar'), data)

    def test_post(self):
        """Invalid POST should not redirect to /inscricao/"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'empresas_cadastro.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_Empresa(self):
        self.assertFalse(EmpresaModel.objects.exists())
