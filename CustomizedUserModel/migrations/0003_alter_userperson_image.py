# Generated by Django 4.0 on 2022-03-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomizedUserModel', '0002_alter_userperson_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='userphoto/', verbose_name='User Photo'),
        ),
    ]