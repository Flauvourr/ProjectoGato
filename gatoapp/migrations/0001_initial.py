# Generated by Django 4.2.5 on 2023-09-30 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_Texto', models.CharField(max_length=160)),
                ('pregunta_Usada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='puntaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_Numero', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_Texto', models.CharField(max_length=100)),
                ('respuesta_Correcto', models.BooleanField(default=False)),
                ('pregunta_Origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatoapp.pregunta')),
            ],
        ),
    ]
