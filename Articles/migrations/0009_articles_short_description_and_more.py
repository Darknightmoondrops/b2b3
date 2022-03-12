# Generated by Django 4.0 on 2022-03-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0008_articleslabels_articles_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='short_description',
            field=models.TextField(blank=True, default='a short description', null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(default='a  description', verbose_name='Description'),
        ),
    ]
