# Generated by Django 4.1 on 2022-09-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventarioApp', '0004_inventario_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='tech',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
