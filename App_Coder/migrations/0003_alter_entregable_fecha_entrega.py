# Generated by Django 4.1.4 on 2023-01-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Coder', '0002_remove_estudiante_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='fecha_entrega',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
