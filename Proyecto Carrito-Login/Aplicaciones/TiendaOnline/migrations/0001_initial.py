# Generated by Django 3.2.8 on 2021-10-30 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='imgMarcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrei', models.CharField(default='', max_length=40)),
                ('fotoi', models.CharField(max_length=300)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipoacces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipocompu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('tel', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
                ('dpi', models.CharField(max_length=300)),
                ('product', models.CharField(max_length=300)),
                ('total', models.CharField(max_length=300)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=300)),
                ('modelo', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('marca', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TiendaOnline.marca')),
                ('tipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TiendaOnline.tipocompu')),
            ],
        ),
        migrations.CreateModel(
            name='accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.CharField(max_length=300)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('marca', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TiendaOnline.marca')),
                ('tipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TiendaOnline.tipoacces')),
            ],
        ),
    ]
