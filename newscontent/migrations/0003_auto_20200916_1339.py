# Generated by Django 3.1.1 on 2020-09-16 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscontent', '0002_auto_20200912_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10)),
                ('value_rur', models.FloatField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 16, 13, 39, 3, 539647)),
        ),
    ]
