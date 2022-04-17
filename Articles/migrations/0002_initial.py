# Generated by Django 4.0 on 2022-04-17 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Articles', '0001_initial'),
        ('CustomizedUserModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleslikes',
            name='like',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomizedUserModel.userperson', verbose_name='Like'),
        ),
        migrations.AddField(
            model_name='articleshits',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Articles.articles', verbose_name='Article'),
        ),
        migrations.AddField(
            model_name='articlescomments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.articles', verbose_name='Article'),
        ),
        migrations.AddField(
            model_name='articlescomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomizedUserModel.userperson', verbose_name='User'),
        ),
        migrations.AddField(
            model_name='articles',
            name='labels',
            field=models.ManyToManyField(to='Articles.ArticlesLabels', verbose_name='Labels'),
        ),
        migrations.AddField(
            model_name='articles',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CustomizedUserModel.userperson', verbose_name='Writer'),
        ),
    ]
