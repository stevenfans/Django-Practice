# Generated by Django 3.0.3 on 2020-02-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restauraunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rating', models.DecimalField(decimal_places=3, max_digits=10)),
                ('phone_num', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
