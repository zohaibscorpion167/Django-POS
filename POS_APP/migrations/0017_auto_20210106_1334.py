# Generated by Django 3.1.1 on 2021-01-06 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0016_auto_20210106_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='item_1',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 6, 13, 34, 50, 224030)),
        ),
    ]
