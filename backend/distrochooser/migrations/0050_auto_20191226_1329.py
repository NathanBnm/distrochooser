# Generated by Django 2.2.8 on 2019-12-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0049_auto_20191226_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='referrer',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]