# Generated by Django 4.0.3 on 2022-04-01 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_composition_icon_composition_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 1, 15, 14, 6, 321479)),
        ),
    ]
