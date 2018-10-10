from django.test import TestCase

from AudiBUN.empresas.form import EmpresaForm


class EmpresaFormTest(TestCase):
    def setUp(self):
        self.form = EmpresaForm()

    def test_form_has_fields(self):
        expected = ['ref_cad', 'name','cnpj','categoria_atividade', 'atividade']
        expected += ['endereco','quadra','lote','categoria_distrito','bairro']
        expected += ['email', 'phone', 'responsavel', 'situacao', 'observacao']
        self.assertSequenceEqual(expected, list(self.form.fields))


class CleanFormTest(TestCase):
    def setUp(self):
        data = {}
        data['ref_cad'] = "12.5.12.01.001"
        data['name'] = "Industria Stark"
        data['cnpj'] = "62.823.257/0001-09"
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


class Test_Field_Ref_Cad_Test(TestCase):
    def setUp(self):
        self.data = {}
        self.data['ref_cad'] = "12.5.12.01.001"
        self.data['name'] = "xxx"
        self.data['cnpj'] = '62.823.257/0001-09'
        self.data['categoria_atividade'] = "prestacao"
        self.data['atividade'] = "xxx"
        self.data['endereco'] = "xxx"
        self.data['quadra'] = "10a"
        self.data['lote'] = "2a"
        self.data['categoria_distrito'] = "0"
        self.data['email'] = ""
        self.data['phone'] = ""
        self.data['responsavel'] = ""
        self.data['situacao'] = "Ativa"
        self.data['observacao'] = ""
        self.form = EmpresaForm(self.data)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_change_ref_cad_invalid_format_1(self):
        self.data['ref_cad'] = "1.1.1.1"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_valid_format_1(self):
        self.data['ref_cad'] = "1.1.1.1.1"
        self.form = EmpresaForm(self.data)
        self.assertEqual(True, self.form.is_valid())

    def test_change_ref_cad_valid_format_2(self):
        self.data['ref_cad'] = "1.1.1.1.1.1"
        self.form = EmpresaForm(self.data)
        self.assertEqual(True, self.form.is_valid())

    def test_change_ref_cad_invalid_format_2(self):
        self.data['ref_cad'] = "1.1.1.1.1.1.1"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_fail_quadricula_subfield(self):
        self.data['ref_cad'] = "A.5.12.01.001"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_fail_zona_subfield(self):
        self.data['ref_cad'] = "1.B.12.01.001"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_fail_setor_subfield(self):
        self.data['ref_cad'] = "1.12.C.01.001"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_fail_lote_subfield(self):
        self.data['ref_cad'] = "1.12.12.01.X"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())


class Test_Field_CNPJ_Test(TestCase):
    def setUp(self):
        self.data = {}
        self.data['ref_cad'] = "12.5.12.01.001"
        self.data['name'] = "xxx"
        self.data['cnpj'] = '62.823.257/0001-09'
        self.data['categoria_atividade'] = "prestacao"
        self.data['atividade'] = "xxx"
        self.data['endereco'] = "xxx"
        self.data['quadra'] = "10a"
        self.data['lote'] = "2a"
        self.data['categoria_distrito'] = "0"
        self.data['email'] = ""
        self.data['phone'] = ""
        self.data['responsavel'] = ""
        self.data['situacao'] = "Ativa"
        self.data['observacao'] = ""
        self.form = EmpresaForm(self.data)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_change_ref_cad_invalid_format_1(self):
        self.data['cnpj'] = "62.8A3.257/0001-09"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_invalid_format_2(self):
        self.data['cnpj'] = "6W2.823.257/0001-09"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_invalid_format_3(self):
        self.data['cnpj'] = "6W2.823.2Q7/0001-09"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_invalid_format_4(self):
        self.data['cnpj'] = "6W2.823.257/0s01-09"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_invalid_format_5(self):
        self.data['cnpj'] = "6W2.823.257/0001-0A"
        self.form = EmpresaForm(self.data)
        self.assertEqual(False, self.form.is_valid())

    def test_change_ref_cad_valid_format_1(self):
        self.data['cnpj'] = "44.333.222/0001-09"
        self.form = EmpresaForm(self.data)
        self.assertEqual(True, self.form.is_valid())
