from datetime import datetime
from django.test import TestCase
from AudiBUN.empresas.models import EmpresaModel, DISTRITO_CHOICES


class EmpresaModelTest(TestCase):
    def setUp(self):
        self.obj = EmpresaModel(
            ref_cad="12.5.12.01.001",
            name="INDUSTRIA STARK LTDA",
            atividade="ATIVIDADE MILITAR",
            endereco="RUA SHIELD, 199",
            quadra="10",
            lote="2",
            categoria_distrito="0",
            email="tony@stark.com",
            phone="055-19-3541-0000",
            responsavel="Anotny Stark",
            observacao="",
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(EmpresaModel.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_distrito_verbose(self):
        distrito = dict(DISTRITO_CHOICES)[self.obj.categoria_distrito]
        self.assertEqual(distrito ,"OUTROS")