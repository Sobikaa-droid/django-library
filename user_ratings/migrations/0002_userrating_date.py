# Generated by Django 4.0.6 on 2023-03-21 03:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrating',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 3, 36, 18, 953506, tzinfo=utc)),
        ),
    ]
