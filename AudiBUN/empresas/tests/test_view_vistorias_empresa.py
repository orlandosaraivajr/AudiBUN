from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, override_settings
from django.shortcuts import resolve_url as r

from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel


TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')

class vistorias_empresaGetFail(TestCase):
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
        self.resp = self.client.get(r('empresas:empresas_vistorias',1) )

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)


class vistorias_empresaGet(TestCase):
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
            responsavel="Anotny Stark"
        )
        self.obj.save()
        self.vistoria = VistoriaModel(
            empresa=self.obj,
            imagem=SimpleUploadedFile('tiny.gif', TINY_GIF)
        )
        self.vistoria.save()
        self.resp = self.client.get(r('empresas:empresas_vistorias', self.obj.pk))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'vistorias_listar_todas.html')

    def test_200_template_empresa(self):
        self.assertEqual(200, self.resp.status_code)

    def test_html(self):
        tags = (
            ('Cadastro de Vistorias', 2),
            ('INDUSTRIA', 1),
            ('STARK', 1),

        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, VistoriaForm)
