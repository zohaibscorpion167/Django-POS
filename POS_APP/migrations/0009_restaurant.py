# Generated by Django 3.1.1 on 2021-01-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0008_auto_20210106_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Order_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
