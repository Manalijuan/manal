# Generated by Django 4.2.3 on 2023-08-01 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto', '0002_vendedor_imagenarticulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='articulo',
            field=models.CharField(choices=[('auto', 'Auto'), ('bicicletas', 'Bicicletas'), ('mostos', 'Motos'), ('monopatines', 'Monopatines'), ('varios', 'Varios')], default='auto', max_length=15),
        ),
    ]
