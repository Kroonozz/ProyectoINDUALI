# Generated by Django 4.1.1 on 2023-07-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]