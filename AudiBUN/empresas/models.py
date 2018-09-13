from django.db.models import Model
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import DateTimeField


class EmpresaModel(Model):
    ref_cad = CharField(max_length=20)
    name = CharField(max_length=100)
    atividade = CharField(max_length=50)
    endereco = CharField(max_length=100)
    quadra = CharField(max_length=10)
    lote = CharField(max_length=10)
    email = EmailField()
    phone = CharField(max_length=20)
    responsavel = CharField(max_length=100)
    situacao = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
