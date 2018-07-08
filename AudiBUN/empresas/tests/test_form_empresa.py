from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm


class EmpresaFormTest(TestCase):
    def setUp(self):
        self.form = EmpresaForm()

    def test_form_has_fields(self):
        """Form must have 4 fields """
        expected = ['ref_cad', 'name', 'atividade', 'endereco']
        expected += ['quadra', 'lote', 'email', 'phone', 'responsavel']
        expected += ['situacao']
        self.assertSequenceEqual(expected, list(self.form.fields))
