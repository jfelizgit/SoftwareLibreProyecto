# Generated by Django 4.1 on 2022-09-02 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventarioApp', '0003_inventario_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='inventario'),
        ),
    ]
