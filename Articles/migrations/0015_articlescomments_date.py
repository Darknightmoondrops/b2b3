# Generated by Django 4.0 on 2022-03-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0014_articlescomments_article_articlescomments_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlescomments',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
    ]
