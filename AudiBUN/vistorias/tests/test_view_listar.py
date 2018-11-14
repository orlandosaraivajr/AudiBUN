from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.shortcuts import resolve_url as r


from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'


class visualizarVistoriaGetFail(TestCase):
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
        self.resp = self.client.get(r('vistorias:vistorias_listar', 1))

    def test_404_template_vistorias(self):
        self.assertEqual(404, self.resp.status_code)

class visualizarVistoriaGet(TestCase):
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
        self.empresa = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
            atividade="ATIVIDADE MILITAR",
            endereco="RUA SHIELD, 199",
            quadra="10",
            lote="2",
            email="tony@stark.com",
            phone="055-19-3541-0000",
            responsavel="Antony Stark",
            observacao="",
        )
        self.empresa.save()
        self.imagem_mock = SimpleUploadedFile('tiny.gif', TINY_GIF)
        self.vistoria = VistoriaModel(
            empresa=self.empresa,
            imagem=self.imagem_mock
        )
        self.vistoria.save()
        self.resp = self.client.get(r('vistorias:vistorias_listar', self.vistoria.pk))

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'vistorias_visualizar.html')

    def test_200_template_vistoria(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Visualizar Vistorias', 2),
            ('readonly', 2),
            ('FATEC Araras', 2),

        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, VistoriaForm)

    def test_has_vistoria(self):
        vistoria = self.resp.context['vistoria']
        self.assertIsInstance(vistoria, VistoriaModel)