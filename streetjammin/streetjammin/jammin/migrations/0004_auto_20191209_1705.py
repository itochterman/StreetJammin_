# Generated by Django 3.0 on 2019-12-09 17:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jammin', '0003_auto_20191209_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 17, 5, 24, 203403, tzinfo=utc)),
        ),
    ]
