from django.db import models

# Create your models here.
class Zapato (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    talla = models.CharField(max_length=2)
    color = models.CharField(max_length=10)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='zapatos', null=True, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Zapato'
        verbose_name_plural = 'Zapatos'

class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Venta (models.Model):
    zapato = models.ForeignKey(Zapato, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return self.zapato.nombre
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'