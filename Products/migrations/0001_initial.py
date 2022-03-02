# Generated by Django 4.0.2 on 2022-03-02 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sellers', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('color_code', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=999, null=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=999)),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('discounted_price', models.IntegerField(blank=True, null=True, verbose_name='Discounted Price')),
                ('score', models.IntegerField(default=1, verbose_name='Score')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('inventory', models.IntegerField(verbose_name='Inventory')),
                ('category', models.ManyToManyField(to='Products.ProductCategories', verbose_name='Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sellers.sellers', verbose_name='Seller')),
            ],
        ),
        migrations.CreateModel(
            name='TrackingCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.CharField(max_length=150, verbose_name='Tracking Code')),
                ('code_status', models.BooleanField(verbose_name='Code Status')),
                ('product_status', models.CharField(choices=[('confirming', 'در حال تایید'), ('confirmed', 'تایید شده'), ('sending', 'در حال ارسال'), ('processed', 'اتمام')], max_length=100, verbose_name='Product_status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(max_length=10, verbose_name='"Total Score')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Products.products', verbose_name='Prodcut ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products', verbose_name='Prodcut Id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
