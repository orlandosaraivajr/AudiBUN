from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.models import VistoriaModel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class VistoriaModelTest(TestCase):
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
        self.vistoria = VistoriaModel(
            empresa=self.empresa,
            imagem=SimpleUploadedFile('tiny.gif', TINY_GIF)
        )
        self.vistoria.save()

    def test_create(self):
        self.assertTrue(EmpresaModel.objects.exists())
        self.assertTrue(VistoriaModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.vistoria.created_at, datetime)

    def test_comentario(self):
        self.assertEqual(self.vistoria.observacao, 'NENHUMA OBSERVAÇÃO')

    def test_empresa(self):
        self.assertEqual(self.vistoria.empresa.id, self.empresa.pk)