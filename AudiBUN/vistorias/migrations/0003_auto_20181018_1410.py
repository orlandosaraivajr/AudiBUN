# Generated by Django 2.1.2 on 2018-10-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistorias', '0002_auto_20181013_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vistoriamodel',
            name='imagem',
            field=models.ImageField(upload_to='imagem/'),
        ),
    ]