# Generated by Django 2.0 on 2019-01-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_perfis_bloqueados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('dt_publicacao', models.DateTimeField()),
            ],
        ),
    ]
