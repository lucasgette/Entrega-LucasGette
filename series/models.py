from django.db import models

# Create your models here.


class Series(models.Model):
    nombre = models.CharField(max_length=35)
    año = models.IntegerField()
    temporadas = models.IntegerField()
    genero = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.nombre} - ({self.año}) - {self.temporadas} temporadas.'
