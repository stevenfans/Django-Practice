# Generated by Django 3.0.1 on 2019-12-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=999)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=999)),
            ],
        ),
    ]
