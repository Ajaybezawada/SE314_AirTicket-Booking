# Generated by Django 3.1.2 on 2022-04-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20220427_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_details',
            name='PassengerCount',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]