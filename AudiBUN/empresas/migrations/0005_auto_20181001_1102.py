# Generated by Django 2.0.6 on 2018-10-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20180928_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresamodel',
            name='bairro',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='categoria_distrito',
            field=models.CharField(choices=[('1', 'DISTRITO 1'), ('2', 'DISTRITO 2'), ('3', 'DISTRITO 3'), ('4', 'DISTRITO 4'), ('5', 'DISTRITO 5'), ('0', 'OUTROS')], default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='observacao',
            field=models.TextField(blank=True, default='NENHUMA OBSERVAÇÃO'),
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='atividade',
            field=models.CharField(default='NÃO DEFINIDA', max_length=50),
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='endereco',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='empresamodel',
            name='responsavel',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
