# Generated by Django 4.0 on 2022-03-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='some string', max_length=200, verbose_name='Site Name')),
                ('payment_token', models.CharField(default='some string', max_length=300, verbose_name='Payment Token')),
                ('site_description', models.TextField(default='some string', verbose_name='Site Description')),
                ('keyword', models.TextField(default='some string', verbose_name='Keyword')),
                ('logo', models.ImageField(upload_to='logo/v1', verbose_name='Logo')),
                ('contact_number', models.CharField(default='123', max_length=15, verbose_name='Contact number')),
                ('address', models.TextField(default='some string', verbose_name='Address')),
                ('email', models.EmailField(default='django@mail.com', max_length=254, verbose_name='Email')),
                ('instagram_link', models.URLField(default='instalink', verbose_name='Instagram')),
                ('android_application_link', models.URLField(default='some string', verbose_name='Android Application')),
            ],
        ),
    ]
