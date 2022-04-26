# Generated by Django 3.0 on 2022-04-26 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CustomizedUserModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=999, verbose_name='Business Name')),
                ('business_description', models.TextField(verbose_name='Business Description')),
                ('business_image', models.ImageField(blank=True, null=True, upload_to='Businessimage', verbose_name='Business Image')),
                ('business_license', models.ImageField(blank=True, null=True, upload_to='BusinessLicenseImage', verbose_name='Business License')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('business_status', models.BooleanField(default=False, verbose_name='business Status')),
                ('business_categories', models.ManyToManyField(to='Sellers.VendorCategories', verbose_name='business Categories')),
                ('business_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomizedUserModel.Userperson', verbose_name='Business Owner')),
            ],
        ),
    ]
