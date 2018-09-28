from django.db.models import Model, CharField, DateTimeField, EmailField

ATIVIDADE_CHOICES = (
    ('prestacao','PRESTAÇÃO DE SERVIÇOS'),
    ('comercio', 'COMÉRCIO'),
    ('industria','INDÚSTRIA'),
)

class EmpresaModel(Model):
    ref_cad = CharField(max_length=20)
    name = CharField(max_length=100)
    categoria_atividade = CharField(max_length=10, \
            choices=ATIVIDADE_CHOICES, default='prestacao')
    atividade = CharField(max_length=50)
    endereco = CharField(max_length=100)
    quadra = CharField(max_length=10)
    lote = CharField(max_length=10)
    email = EmailField()
    phone = CharField(max_length=20)
    responsavel = CharField(max_length=100)
    situacao = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)

