# Generated by Django 3.1 on 2020-08-09 10:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0002_auto_20200809_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='newscontent.section'),
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 14, 26, 30, 966873)),
        ),
    ]
