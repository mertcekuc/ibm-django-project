# Generated by Django 3.1.3 on 2023-08-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230808_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=25),
        ),
    ]
