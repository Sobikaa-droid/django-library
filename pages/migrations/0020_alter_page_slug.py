# Generated by Django 4.2 on 2023-04-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_alter_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]