# Generated by Django 4.0.6 on 2023-03-28 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_delete_userrating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-pk']},
        ),
    ]