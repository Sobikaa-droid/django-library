# Generated by Django 4.2 on 2023-04-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]