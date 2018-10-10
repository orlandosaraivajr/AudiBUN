from unittest import mock

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')

class Test_Field_Ref_Cad_Test(TestCase):
    def setUp(self):
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
            situacao="Ativa",
            observacao="",
        )
        self.empresa.save()
        file_mock = SimpleUploadedFile('tiny.gif', TINY_GIF)
        self.vistoria = {
            'observacao':"aaa",
            'empresa':self.empresa.id,
            'imagem':file_mock,
        }
        self.form = VistoriaForm(self.vistoria)
        self.form.is_valid()
        self.form.save()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_create(self):
        self.assertTrue(EmpresaModel.objects.exists())
        self.assertTrue(VistoriaModel.objects.exists())
