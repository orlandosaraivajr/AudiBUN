from django.test import TestCase, override_settings
from django.shortcuts import resolve_url as r


class clistarVistoriasGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('vistorias:vistorias_listar_todas'))

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'vistorias_listar_todas.html')

    def test_200_template_home(self):
        self.assertEqual(200, self.resp.status_code)

    def test_labels_html(self):
        tags = (
            ('Cadastro de Vistorias', 2),
            ('FATEC Araras', 2),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

