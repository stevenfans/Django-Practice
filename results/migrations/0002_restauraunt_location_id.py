# Generated by Django 3.0.3 on 2020-03-11 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restauraunt',
            name='location_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
            preserve_default=False,
        ),
    ]