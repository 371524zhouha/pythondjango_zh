# Generated by Django 2.1.4 on 2019-03-30 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20190325_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 10, 32, 36, 356974, tzinfo=utc)),
        ),
    ]
