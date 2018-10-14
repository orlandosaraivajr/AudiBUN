from django.test import TestCase
from django.shortcuts import resolve_url as r
from AudiBUN.vistorias.form import VistoriaForm


class cadastroVistoriasGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('vistorias:vistorias_cadastrar'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'vistorias_cadastro.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('Vistorias', 3),
            ('Foto', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 3),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, VistoriaForm)

'''
class cadastroEmpresaPostValid(TestCase):
    def setUp(self):
        data = {}
        data['ref_cad'] = "12.5.12.01.001"
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
        data['situacao'] = "Ativa"
        data['observacao'] = "1"
        self.resp = self.client.post(r('empresas:empresas_cadastrar'), data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_save_Empresa(self):
        self.assertTrue(EmpresaModel.objects.exists())


class cadastroEmpresaPostInvalid(TestCase):
    def setUp(self):
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
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_Empresa(self):
        self.assertFalse(EmpresaModel.objects.exists())
'''