# Generated by Django 4.0 on 2022-04-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_alter_products_colors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(blank=True, to='Products.ProductsColor', verbose_name='Colors'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='Products.ProductsSizes', verbose_name='Sizes'),
        ),
    ]
