# Generated by Django 3.1.1 on 2021-01-06 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0009_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='order_date',
            field=models.DateField(default=datetime.date(2021, 1, 6)),
        ),
    ]
