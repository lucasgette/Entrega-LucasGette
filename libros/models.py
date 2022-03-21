from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=35)
    autor = models.CharField(max_length=20)
    publicacion = models.IntegerField()
    genero = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.nombre} - {self.autor}'

