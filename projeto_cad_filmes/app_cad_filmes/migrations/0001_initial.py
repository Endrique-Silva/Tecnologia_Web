# Generated by Django 4.2.4 on 2023-08-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id_filme', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
                ('descrição', models.TextField(max_length=255)),
                ('duração', models.FloatField()),
            ],
        ),
    ]