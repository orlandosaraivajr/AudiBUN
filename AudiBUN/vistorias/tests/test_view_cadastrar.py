from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings, Client
from django.shortcuts import resolve_url as r

from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class cadastroVistoriasGet(TestCase):
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
        self.resp = self.client.get(r('vistorias:vistorias_cadastrar'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'vistorias_cadastro.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('Vistorias', 2),
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

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class cadastroVistoriaPostValid(TestCase):
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
            atividade="ATIVIDADE MILITAR",
            endereco="RUA SHIELD, 199",
            quadra="10",
            lote="2",
            email="tony@stark.com",
            phone="055-19-3541-0000",
            responsavel="Antony Stark",
            observacao="",
        )
        self.obj.save()
        self.imagem_mock = SimpleUploadedFile('tiny.gif', TINY_GIF)

        self.data = {}
        self.data['empresa'] = self.obj.pk
        self.data['observacao'] = "agendado próxima visita"
        self.data['imagem'] = self.imagem_mock

        self.resp = self.client.post(r('vistorias:vistorias_cadastrar'), self.data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_saved_data(self):
        self.assertTrue(EmpresaModel.objects.exists())
        self.assertTrue(VistoriaModel.objects.exists())


class cadastroVistoriaPostInvalidImage(TestCase):
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
            atividade="ATIVIDADE MILITAR",
            endereco="RUA SHIELD, 199",
            quadra="10",
            lote="2",
            email="tony@stark.com",
            phone="055-19-3541-0000",
            responsavel="Antony Stark",
            observacao="",
        )
        self.obj.save()

        self.data = {}
        self.data['empresa'] = self.obj.pk
        self.data['observacao'] = "agendado próxima visita"
        self.data['imagem'] = None
        self.resp = self.client.post(r('vistorias:vistorias_cadastrar'), self.data)

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_saved_data(self):
        self.assertTrue(EmpresaModel.objects.exists())
        self.assertFalse(VistoriaModel.objects.exists())

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)
