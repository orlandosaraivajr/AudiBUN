from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


class visualizarEmpresaGetFail(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastroEmpresa/1')

    def test_301_response(self):
        self.assertEqual(301, self.resp.status_code)


class visualizarEmpresaGetGet(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
            categoria_atividade="prestacao",
            atividade="ATIVIDADE MILITAR",
            endereco="RUA SHIELD, 199",
            quadra="10",
            lote="2",
            email="tony@stark.com",
            phone="055-19-3541-0000",
            responsavel="Anotny Stark",
            situacao="Ativa"
        )
        self.obj.save()
        self.resp = self.client.get('/cadastroEmpresa/1/')

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'visualizar.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Visualizar cadastro da Empresa', 2),
            ('readonly', 14),

        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)
