# Generated by Django 2.2.10 on 2021-06-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_paquete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete',
            name='producto_id',
        ),
        migrations.AddField(
            model_name='paquete',
            name='producto_id',
            field=models.ManyToManyField(to='ecom.Product'),
        ),
    ]