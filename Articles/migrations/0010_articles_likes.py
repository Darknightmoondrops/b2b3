# Generated by Django 4.0 on 2022-03-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0009_articles_short_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Likes'),
        ),
    ]