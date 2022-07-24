from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    fechaDeNacimiento=models.DateField()
    def __str__(self):
            return f"Nombre:{self.nombre} - Edad {self.edad} - Nacimiento {self.fechaDeNacimiento}"

class Animales(models.Model):
    nombre=models.CharField(max_length=20)
    fechaDeNacimiento=models.DateField()
    tipo=models.CharField(max_length=20)
    def __str__(self):
            return f"Nombre:{self.nombre} - Nacimiento {self.fechaDeNacimiento} - tipo {self.tipo}"

class Vehiculos(models.Model):
    kilometraje=models.IntegerField()
    modelo=models.IntegerField()
    tipo=models.CharField(max_length=20)
    def __str__(self):
            return f"Kilometraje:{self.kilometraje} - Modelo {self.modelo} - tipo {self.tipo}"
        

class Avatar(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title