from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')

class Test_VistoriaForm_Test(TestCase):
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
            observacao="",
        )
        self.empresa.save()
        self.mocked_img = SimpleUploadedFile('tiny.gif', TINY_GIF)
        self.vistoria = {
            'observacao':"aaa",
            'empresa':self.empresa.id
        }
        self.imagem = {
            'imagem':self.mocked_img
        }
        self.form = VistoriaForm(self.vistoria, self.imagem)
        self.form.is_valid()
        self.form.save()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_create(self):
        self.assertTrue(EmpresaModel.objects.exists())
        self.assertTrue(VistoriaModel.objects.exists())

    def test_saved_image(self):
        self.assertEqual(self.mocked_img, self.form.cleaned_data['imagem'])

    def test_observacao_upper(self):
        self.assertEqual('AAA', self.form.cleaned_data['observacao'])

    def test_method_read_only_true(self):
        self.form.read_only()
        fields = list(self.form.fields)
        for field in fields:
            with self.subTest():
                self.assertEqual(self.form.fields[field].widget.attrs['readonly'], True)

    def test_method_read_only_false(self):
        self.form.read_only(False)
        fields = list(self.form.fields)
        for field in fields:
            with self.subTest():
                self.assertEqual(self.form.fields[field].widget.attrs['readonly'], False)


class Test_VistoriaForm_NoImage_Test(TestCase):
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
            observacao="",
        )
        self.empresa.save()
        self.mocked_img = SimpleUploadedFile('tiny.gif', TINY_GIF)
        self.vistoria = {
            'observacao':"aaa",
            'empresa':self.empresa.id
        }

        self.form = VistoriaForm(self.vistoria)
        self.form.is_valid()
        self.form.save()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_create(self):
        self.assertTrue(EmpresaModel.objects.exists())
        self.assertTrue(VistoriaModel.objects.exists())

    def test_saved_image(self):
        self.assertEqual(None, self.form.cleaned_data['imagem'])

    def test_observacao_upper(self):
        self.assertEqual('AAA', self.form.cleaned_data['observacao'])

    def test_method_read_only_true(self):
        self.form.read_only()
        fields = list(self.form.fields)
        for field in fields:
            with self.subTest():
                self.assertEqual(self.form.fields[field].widget.attrs['readonly'], True)

    def test_method_read_only_false(self):
        self.form.read_only(False)
        fields = list(self.form.fields)
        for field in fields:
            with self.subTest():
                self.assertEqual(self.form.fields[field].widget.attrs['readonly'], False)
