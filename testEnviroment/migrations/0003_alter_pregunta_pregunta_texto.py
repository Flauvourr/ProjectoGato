# Generated by Django 4.2.5 on 2023-09-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testEnviroment', '0002_pregunta_pregunta_usada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta_Texto',
            field=models.CharField(max_length=160),
        ),
    ]
