# Generated by Django 4.1.1 on 2022-11-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroCosto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codCentroCostos', models.CharField(max_length=50, verbose_name='Codigo Centro de Costos')),
                ('nomCentroCostos', models.CharField(max_length=50, verbose_name='Nommbre Centro de Costos')),
                ('nomEmpresa', models.CharField(max_length=50, verbose_name='Nombre Empresa')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
    ]
