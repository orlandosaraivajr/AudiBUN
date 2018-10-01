from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm


class EmpresaFormTest(TestCase):
    def setUp(self):
        self.form = EmpresaForm()

    def test_form_has_fields(self):
        """Form must have 4 fields """
        expected = ['ref_cad', 'name','categoria_atividade', 'atividade']
        expected += ['endereco','quadra','lote','categoria_distrito','bairro']
        expected += ['email', 'phone', 'responsavel', 'situacao', 'observacao']
        self.assertSequenceEqual(expected, list(self.form.fields))
