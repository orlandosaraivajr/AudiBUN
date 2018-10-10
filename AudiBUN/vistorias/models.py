from django.db.models import Model, ForeignKey, CASCADE, DateTimeField, TextField, ImageField
from AudiBUN.empresas.models import EmpresaModel


class VistoriaModel(Model):
    empresa = ForeignKey(EmpresaModel, on_delete=CASCADE)
    imagem = ImageField(upload_to='image/', blank=True)
    observacao = TextField(default='NENHUMA OBSERVAÇÃO', blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa_id