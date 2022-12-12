# Generated by Django 4.1.1 on 2022-11-24 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0003_alter_usuario_estado_alter_usuario_numerodocumento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='numeroDocumento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='correoElectronico',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(default=1, max_length=50, verbose_name='Apellidos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombreUsuario',
            field=models.CharField(default=1, max_length=50, verbose_name='Nombre Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(default=1, max_length=50, verbose_name='Nombres'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('P.A', 'Pasaporte'), ('Otro', 'Otro Tipo de Documento')], default='C.C', max_length=20, verbose_name='Tipo Documento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Estandar', 'Estandar'), ('Invitado', 'Invitado')], default='Invitado', max_length=20, verbose_name='Tipo Usuario'),
        ),
    ]