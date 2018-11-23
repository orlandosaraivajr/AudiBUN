from django.db.models import Model, CharField, DateTimeField, EmailField, TextField

ATIVIDADE_CHOICES = (
    ('prestacao','PRESTAÇÃO DE SERVIÇOS'),
    ('comercio', 'COMÉRCIO'),
    ('industria','INDÚSTRIA'),
)

DISTRITO_CHOICES = (
    ('1','DISTRITO I'),
    ('2', 'DISTRITO II'),
    ('3', 'DISTRITO III'),
    ('4', 'DISTRITO IV'),
    ('5', 'DISTRITO V'),
    ('5', 'DISTRITO VI'),
    ('0','OUTROS'),
)

class EmpresaModel(Model):
    ref_cad = CharField(max_length=20)
    area_lote = CharField(max_length=20, default='')
    area_construida = CharField(max_length=20, default='')
    name = CharField(max_length=100)
    cnpj = CharField(max_length=20, default='00.000.000/0000-00')
    categoria_atividade = CharField(max_length=10, \
            choices=ATIVIDADE_CHOICES, default='prestacao')
    atividade = CharField(default='NÃO DEFINIDA', blank=False, max_length=200)
    endereco = CharField(blank=True, max_length=100)
    quadra = CharField(blank=False, max_length=10)
    lote = CharField(blank=False, max_length=10)
    categoria_distrito = CharField(max_length=2, \
                                    choices=DISTRITO_CHOICES, default='0')
    bairro = CharField(blank=True, max_length=100)
    email = EmailField(blank=True)
    phone = CharField(max_length=20, blank=True)
    responsavel = CharField(blank=True, max_length=100)
    observacao = TextField(default='NENHUMA OBSERVAÇÃO', blank=True)
    created_at = DateTimeField(auto_now_add=True)


    def distrito_verbose(self):
        return dict(DISTRITO_CHOICES)[self.categoria_distrito]

    def __str__(self):
        return self.name


    def __unicode__(self):
        return u"%s" % self.name