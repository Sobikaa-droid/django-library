# Generated by Django 4.0.6 on 2023-03-08 01:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_description_alter_page_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='rating',
            new_name='average_rating',
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
            options={
                'ordering': ['page__name'],
            },
        ),
    ]