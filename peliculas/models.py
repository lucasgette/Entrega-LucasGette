from django.db import models

# Create your models here.


class Peliculas(models.Model):
    nombre = models.CharField(max_length=35)
    director = models.CharField(max_length=20)
    año = models.IntegerField()
    genero = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.nombre} - {self.director} ({self.año})'






    
