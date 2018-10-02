from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm


class EmpresaFormTest(TestCase):
    def setUp(self):
        self.form = EmpresaForm()

    def test_form_has_fields(self):
        expected = ['ref_cad', 'name','categoria_atividade', 'atividade']
        expected += ['endereco','quadra','lote','categoria_distrito','bairro']
        expected += ['email', 'phone', 'responsavel', 'situacao', 'observacao']
        self.assertSequenceEqual(expected, list(self.form.fields))


class CleanFormTest(TestCase):
    def setUp(self):
        data = {}
        data['ref_cad'] = "12.5.12.01.001"
        data['name'] = "Industria Stark"
        data['categoria_atividade'] = "prestacao"
        data['atividade'] = "aTIVIdAde Militar"
        data['endereco'] = "RUA Shield, 199"
        data['quadra'] = "10a"
        data['lote'] = "2a"
        data['categoria_distrito'] = "0"
        data['email'] = "tony@stark.com"
        data['phone'] = "055-19-3541-0000"
        data['responsavel'] = "Antony Stark"
        data['situacao'] = "Ativa"
        data['observacao'] = "instalação em novembro de 2017"
        self.form = EmpresaForm(data)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_name_upper(self):
        self.assertEqual('INDUSTRIA STARK', self.form.cleaned_data['name'])

    def test_atividade_upper(self):
        self.assertEqual('ATIVIDADE MILITAR', self.form.cleaned_data['atividade'])

    def test_endereco_upper(self):
        self.assertEqual('RUA SHIELD, 199', self.form.cleaned_data['endereco'])

    def test_quadra_upper(self):
        self.assertEqual('10A', self.form.cleaned_data['quadra'])

    def test_lote_upper(self):
        self.assertEqual('2A', self.form.cleaned_data['lote'])

    def test_responsavel_upper(self):
        self.assertEqual('ANTONY STARK', self.form.cleaned_data['responsavel'])

    def test_situacao_upper(self):
        self.assertEqual('ATIVA', self.form.cleaned_data['situacao'])

    def test_observacao_upper(self):
        self.assertEqual('INSTALAÇÃO EM NOVEMBRO DE 2017', self.form.cleaned_data['observacao'])

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
