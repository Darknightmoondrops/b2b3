# Generated by Django 4.0 on 2022-04-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerificationCodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codes',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Status'),
        ),
    ]