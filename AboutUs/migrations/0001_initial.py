# Generated by Django 3.0 on 2022-04-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('team_image', models.ImageField(upload_to='static_cdn/media_root/TeamImage')),
            ],
        ),
    ]
