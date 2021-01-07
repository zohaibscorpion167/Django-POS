# Generated by Django 3.1.1 on 2021-01-07 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0021_auto_20210106_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Received_By',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='order_date',
            field=models.DateField(default=datetime.date(2021, 1, 7)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 7, 12, 33, 26, 67570)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date_added',
            field=models.DateField(default=datetime.date(2021, 1, 7)),
        ),
    ]
