# Generated by Django 4.0.6 on 2023-03-22 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_ratings', '0003_alter_userrating_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrating',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='userrating',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
