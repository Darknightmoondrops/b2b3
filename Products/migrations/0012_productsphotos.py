# Generated by Django 4.0 on 2022-03-16 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_products_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ProductsPhotos', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products', verbose_name='Product')),
            ],
        ),
    ]