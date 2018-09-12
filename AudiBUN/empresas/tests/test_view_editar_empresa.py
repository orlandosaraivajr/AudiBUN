from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


class editarEmpresasGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/editarEmpresa/')

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas.html')

    def test_200_template_empresas(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Editar Empresas', 2),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)


class editarEmpresaGet(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
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
        self.resp = self.client.get('/editarEmpresa/1/')

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'editar.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Editar cadastro da Empresa', 2),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, EmpresaForm)


class editarEmpresaGetNoData(TestCase):
    def setUp(self):
        self.resp = self.client.get('/editarEmpresa/1/')

    def test_404_template_empresa(self):
        self.assertEqual(404, self.resp.status_code)

class editarEmpresaPost(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
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
        d = {'ref_cad': '123.45',
             'name': 'Ozark',
             'atividade': 'lavagem de dinheiro',
             'endereco': 'Rua elo Horizonte',
             'quadra': '102',
             'lote': '20',
             'email': 'zeninguem@terra.mx',
             'phone': '055-19-3541-0000',
             'responsavel': 'desconhecido',
             'situacao': 'Ativa'
        }
        self.resp = self.client.post('/editarEmpresa/1/', d)

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'editar.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_data_changed_name(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].name, 'Ozark')

    def test_data_changed_email(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].email, 'zeninguem@terra.mx')


class editarEmpresaPostFail(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
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
        d = {'ref_cad': '123.45',
             'atividade': 'lavagem de dinheiro',
             'endereco': 'Rua elo Horizonte',
             'quadra': '102',
             'lote': '20',
             'email': 'zeninguem@terra.mx',
             'phone': '055-19-3541-0000',
             'responsavel': 'desconhecido',
             'situacao': 'Ativa'
        }
        self.resp = self.client.post('/editarEmpresa/1/', d)

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_data_changed_name(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].name, 'INDUSTRIA STARK LTDA')

    def test_data_changed_email(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].email, 'tony@stark.com')