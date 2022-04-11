# Generated by Django 4.0 on 2022-04-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CustomizedUserModel', '0004_alter_userperson_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=999, null=True, verbose_name='Title service')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Services', verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('score', models.IntegerField(blank=True, default=1, null=True, verbose_name='Score')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('categories', models.ManyToManyField(to='Services.ServiceCategories', verbose_name='Categories')),
                ('service_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomizedUserModel.userperson', verbose_name='service user')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='ProductsCommentsImage', verbose_name='Image')),
                ('service_title', models.TextField(blank=True, null=True, verbose_name='Title')),
                ('service_short_description', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.services', verbose_name='Services Id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomizedUserModel.userperson', verbose_name='User')),
            ],
        ),
    ]