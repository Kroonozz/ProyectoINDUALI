# Generated by Django 4.1.2 on 2023-02-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0005_remove_ingrediente_cantidadmateriaprima_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
    ]
