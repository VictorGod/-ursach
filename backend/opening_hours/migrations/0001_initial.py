# Generated by Django 4.1.4 on 2022-12-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opening_Hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monday', models.CharField(max_length=255, verbose_name='Понедельник')),
                ('Tuesday', models.CharField(max_length=255, verbose_name='Вторник')),
                ('Wednesday', models.CharField(max_length=255, verbose_name='Среда')),
                ('Thursday', models.CharField(max_length=255, verbose_name='Четверг')),
                ('Friday', models.CharField(max_length=255, verbose_name='Пятница')),
                ('Saturday', models.CharField(max_length=255, verbose_name='Суббота')),
                ('Sunday', models.CharField(max_length=255, verbose_name='Воскресенье')),
            ],
        ),
    ]
