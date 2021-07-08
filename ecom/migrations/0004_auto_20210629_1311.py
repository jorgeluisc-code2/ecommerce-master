# Generated by Django 2.2.10 on 2021-06-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_auto_20210628_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='NombreProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=350)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ManyToManyField(to='ecom.Product'),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='paquete_imagen',
            field=models.ImageField(blank=True, default='static/paquete.png', null=True, upload_to='paquete_image/'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.ManyToManyField(to='ecom.NombreProducto'),
        ),
    ]