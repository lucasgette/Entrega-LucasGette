# Generated by Django 4.0.3 on 2022-03-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('año', models.IntegerField()),
                ('temporadas', models.IntegerField()),
                ('genero', models.CharField(max_length=35)),
            ],
        ),
    ]
