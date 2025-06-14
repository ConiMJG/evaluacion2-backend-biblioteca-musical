# Generated by Django 4.2.23 on 2025-06-11 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('artista', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('duracion', models.PositiveIntegerField(help_text='Duranción en segundos', validators=[django.core.validators.MinValueValidator(1)])),
                ('anio_lanzamiento', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2025)])),
                ('calificacion', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('favorita', models.BooleanField(default=False)),
                ('reproducciones', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Canción',
                'verbose_name_plural': 'Canciones',
            },
        ),
    ]
