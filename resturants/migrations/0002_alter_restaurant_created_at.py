# Generated by Django 4.1.2 on 2022-10-11 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 11, 17, 17, 44, 46842)),
        ),
    ]
