# Generated by Django 4.0.4 on 2022-04-30 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        ('Sellers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_created=True, verbose_name='Payment Date')),
                ('payment_status', models.BooleanField(default=True, verbose_name='Payment Status')),
                ('shoper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Shoper')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_created=True, verbose_name='Payment Date')),
                ('title', models.CharField(blank=True, max_length=999, null=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('discounted_price', models.IntegerField(blank=True, null=True, verbose_name='Discounted Price')),
                ('score', models.IntegerField(default=1, verbose_name='Score')),
                ('product_id', models.IntegerField(blank=True, null=True, verbose_name='Product id')),
                ('payment_status', models.BooleanField(default=True, verbose_name='Payment Status')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carts.carts', verbose_name='Cart')),
                ('category', models.ManyToManyField(to='Products.productsubcategories_1', verbose_name='Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sellers.sellers', verbose_name='Seller')),
            ],
        ),
    ]
