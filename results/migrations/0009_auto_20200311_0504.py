# Generated by Django 3.0.3 on 2020-03-11 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roulette', '0003_auto_20200302_0508'),
        ('results', '0008_auto_20200311_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restauraunt',
            name='foreign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roulette.Location'),
        ),
    ]
