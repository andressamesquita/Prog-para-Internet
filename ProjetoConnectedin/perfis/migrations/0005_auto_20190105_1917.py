# Generated by Django 2.0 on 2019-01-05 21:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_postagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='responsavel',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='minhas_postagens', to='perfis.Perfil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postagem',
            name='dt_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 5, 19, 16, 48, 730854)),
        ),
    ]
