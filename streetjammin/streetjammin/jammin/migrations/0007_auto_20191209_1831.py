# Generated by Django 3.0 on 2019-12-09 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jammin', '0006_auto_20191209_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 18, 31, 48, 658183, tzinfo=utc)),
        ),
    ]