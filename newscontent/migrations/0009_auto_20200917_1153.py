# Generated by Django 3.1.1 on 2020-09-17 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0008_auto_20200917_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='valute_name',
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 11, 53, 4, 547039)),
        ),
    ]