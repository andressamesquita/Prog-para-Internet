# Generated by Django 2.0 on 2019-01-06 04:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0011_auto_20190106_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='dt_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 6, 4, 14, 31, 607507, tzinfo=utc)),
        ),
    ]
