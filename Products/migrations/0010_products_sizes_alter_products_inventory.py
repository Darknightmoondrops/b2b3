# Generated by Django 4.0 on 2022-03-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_productssizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='Products.ProductsSizes', verbose_name='Sizes'),
        ),
        migrations.AlterField(
            model_name='products',
            name='inventory',
            field=models.IntegerField(default=0, verbose_name='Inventory'),
        ),
    ]