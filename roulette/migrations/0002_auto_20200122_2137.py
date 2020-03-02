# Generated by Django 3.0.2 on 2020-01-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulette', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=20),
        ),
    ]
