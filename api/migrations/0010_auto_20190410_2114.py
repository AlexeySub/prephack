# Generated by Django 2.1.7 on 2019-04-10 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190410_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 10, 21, 14, 39, 302601)),
        ),
    ]
