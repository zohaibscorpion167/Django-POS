# Generated by Django 3.1.1 on 2021-01-05 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('received_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('date_added', models.DateField(default='2021-01-01', verbose_name=datetime.datetime(2021, 1, 5, 14, 30, 32, 439747))),
            ],
        ),
    ]
