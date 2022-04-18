# Generated by Django 4.0 on 2022-04-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_products_maincategories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(blank=True, to='Products.ProductsColor', verbose_name='Colors'),
        ),
        migrations.AlterField(
            model_name='products',
            name='maincategories',
            field=models.ManyToManyField(blank=True, to='Products.ProductMainCategories', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='Products.ProductsSizes', verbose_name='Sizes'),
        ),
        migrations.AlterField(
            model_name='products',
            name='subCategories1',
            field=models.ManyToManyField(blank=True, to='Products.ProductSubCategories_1', verbose_name='Sub Category 1'),
        ),
        migrations.AlterField(
            model_name='products',
            name='subCategories2',
            field=models.ManyToManyField(blank=True, to='Products.ProductSubCategories_2', verbose_name='Sub Category 2'),
        ),
    ]
