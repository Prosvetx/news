# Generated by Django 3.1.1 on 2020-09-29 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0013_auto_20200919_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 15, 12, 14, 158640)),
        ),
        migrations.AlterField(
            model_name='rate',
            name='valute_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
