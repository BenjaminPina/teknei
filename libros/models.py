from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    portada = models.ImageField(blank=True, null=True)
    categorias = models.ManyToManyField(Categoria, related_name='libros')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo
