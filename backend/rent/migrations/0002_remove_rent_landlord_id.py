# Generated by Django 4.1.4 on 2023-01-12 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='landlord_id',
        ),
    ]
