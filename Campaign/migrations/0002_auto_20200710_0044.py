# Generated by Django 3.0.7 on 2020-07-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
