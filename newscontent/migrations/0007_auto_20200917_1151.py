# Generated by Django 3.1.1 on 2020-09-17 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0006_auto_20200917_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 11, 51, 13, 630635)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='valute_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
