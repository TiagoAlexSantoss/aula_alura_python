# Generated by Django 5.0.1 on 2024-02-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='nome',
            field=models.CharField(default='padrao', max_length=100),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.CharField(max_length=150),
        ),
    ]