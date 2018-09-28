from django.db import models

ATIVIDADE_CHOICES = (
    ('prestacao','PRESTAÇÃO DE SERVIÇOS'),
    ('comercio', 'COMÉRCIO'),
    ('industria','INDÚSTRIA'),
)

class EmpresaModel(models.Model):
    ref_cad = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    categoria_atividade = models.CharField(max_length=10, \
            choices=ATIVIDADE_CHOICES, default='prestacao')
    atividade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    quadra = models.CharField(max_length=10)
    lote = models.CharField(max_length=10)
    email =  models.EmailField()
    phone = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=100)
    situacao = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
