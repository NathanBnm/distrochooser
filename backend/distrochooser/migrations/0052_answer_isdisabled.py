# Generated by Django 2.2.8 on 2020-01-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0051_answer_mediasourcepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='isDisabled',
            field=models.BooleanField(default=False),
        ),
    ]