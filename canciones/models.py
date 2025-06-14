from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)

    duracion = models.PositiveIntegerField(
        help_text="Duranción en segundos", 
        validators=[MinValueValidator(1)]
    )

    anio_lanzamiento = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)]
    )

    calificacion = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    favorita = models.BooleanField(default=False)
    reproducciones = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
    
    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"