# Generated by Django 3.1.1 on 2021-01-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0013_auto_20210106_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Order_ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='Order ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='item_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
