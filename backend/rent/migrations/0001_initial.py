# Generated by Django 4.1.4 on 2022-12-29 11:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landlord', '0001_initial'),
        ('payment', '0001_initial'),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_data', models.DateField(verbose_name='начало аредны')),
                ('end_data', models.CharField(max_length=255, verbose_name='конец аредны')),
                ('client_id', models.ManyToManyField(related_name='Rent', to=settings.AUTH_USER_MODEL)),
                ('landlord_id', models.ManyToManyField(related_name='Rent', to='landlord.landlord')),
                ('payment', models.ManyToManyField(related_name='Rent', to='payment.payment')),
                ('place', models.ManyToManyField(related_name='Rent', to='place.place')),
            ],
        ),
    ]
