# Generated by Django 2.1.2 on 2018-11-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0007_auto_20181114_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresamodel',
            name='area_construida',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='area_lote',
            field=models.CharField(default='', max_length=20),
        ),
    ]
