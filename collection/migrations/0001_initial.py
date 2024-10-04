# Generated by Django 5.1.1 on 2024-10-02 02:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Fragrance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('time_of_day', models.CharField(choices=[('d', 'Day'), ('n', 'Night')], max_length=1)),
                ('seasons_of_year', models.CharField(choices=[('S', 'summer'), ('F', 'fall'), ('W', 'winter'), ('p', 'sprint')], max_length=1)),
                ('reting', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comments', models.TextField()),
                ('bran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.brand', verbose_name='brand')),
                ('notes', models.ManyToManyField(to='collection.note', verbose_name='Notes')),
            ],
        ),
    ]
