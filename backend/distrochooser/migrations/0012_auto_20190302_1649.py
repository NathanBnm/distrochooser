# Generated by Django 2.1.2 on 2019-03-02 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0011_auto_20190302_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 2, 16, 49, 26, 76185)),
        ),
    ]
