from django.test import TestCase
from django.shortcuts import resolve_url as r
from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


class editarEmpresasGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('empresas:empresas_listar_editar'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas_listar_editar.html')

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
            cnpj="62.823.257/0001-09",
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
        self.resp = self.client.get(r('empresas:editar', self.obj.pk))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas_editar.html')

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
        data = {'id_empresa':'1'}
        self.resp = self.client.get(r('empresas:editar', 1))

    def test_404_template_empresa(self):
        self.assertEqual(404, self.resp.status_code)

class editarEmpresa_accept_blank_Post(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
            atividade="ATIVIDADE MILITAR",
            cnpj="62.823.257/0001-09",
            endereco="",
            quadra="10",
            lote="2",
            categoria_distrito="0",
            email="",
            phone="",
            responsavel="",
            situacao="Ativa",
            observacao=""
        )
        self.obj.save()
        d = {'ref_cad': '12.5.12.01.002',
             'name': 'Ozark',
             'categoria_atividade': 'comercio',
             'atividade': 'lavagem de dinheiro',
             'cnpj': '62.823.257/0001-09',
             'endereco': 'Rua Belo Horizonte',
             'quadra': '102',
             'lote': '20',
             'categoria_distrito': '1',
             'email': 'zeninguem@terra.mx',
             'phone': '055-19-3541-0000',
             'responsavel': 'desconhecido',
             'situacao': 'Ativa',
             'observacao': ''}

        self.resp = self.client.post(r('empresas:editar', self.obj.pk), d)

    def test_data_changed_name(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].name, 'OZARK')

    def test_data_changed_email(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].email, 'zeninguem@terra.mx')

    def test_data_changed_categoria_atividade(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].categoria_atividade, 'comercio')

class editarEmpresaPost(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
            cnpj="62.823.257/0001-09",
            atividade="ATIVIDADE MILITAR",
            endereco="RUA SHIELD, 199",
            quadra="10",
            lote="2",
            categoria_distrito="0",
            email="tony@stark.com",
            phone="055-19-3541-0000",
            responsavel="Anotny Stark",
            situacao="Ativa",
            observacao="teste"
        )
        self.obj.save()
        d = {'ref_cad': '12.5.12.01.002',
             'name': 'Ozark',
             'cnpj': '62.823.257/0001-09',
             'categoria_atividade': 'comercio',
             'atividade': 'lavagem de dinheiro',
             'endereco': 'Rua elo Horizonte',
             'quadra': '102',
             'lote': '20',
             'categoria_distrito': '0',
             'email': 'zeninguem@terra.mx',
             'phone': '055-19-3541-0000',
             'responsavel': 'desconhecido',
             'situacao': 'Ativa',
             'observacao': ''}
        self.resp = self.client.post(r('empresas:editar', self.obj.pk), d)

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas_editar.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_data_changed_name(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].name, 'OZARK')

    def test_data_changed_email(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].email, 'zeninguem@terra.mx')

    def test_data_changed_categoria_atividade(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].categoria_atividade, 'comercio')

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
        d = {'ref_cad': '12.5.12.01.002',
             'atividade': 'lavagem de dinheiro',
             'endereco': 'Rua elo Horizonte',
             'quadra': '102',
             'lote': '20',
             'email': 'zeninguem@terra.mx',
             'phone': '055-19-3541-0000',
             'responsavel': 'desconhecido',
             'situacao': 'Ativa'}
        self.resp = self.client.post(r('empresas:editar', self.obj.pk), d)

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'empresas_editar.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_data_not_changed_name(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].name, 'INDUSTRIA STARK LTDA')

    def test_data_not_changed_email(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].email, 'tony@stark.com')

    def test_data_not_changed_categoria_atividade(self):
        q = EmpresaModel.objects.filter(pk=1)
        self.assertEqual(q[0].categoria_atividade, 'prestacao')
