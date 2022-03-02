# Generated by Django 4.0.2 on 2022-03-02 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_created=True, verbose_name='Payment Date')),
                ('payment_status', models.BooleanField(default=True, verbose_name='Payment Status')),
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
                ('payment_status', models.BooleanField(default=True, verbose_name='Payment Status')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carts.carts', verbose_name='Cart')),
            ],
        ),
    ]