from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(default='')
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='imagenes/')
    categoria = models.CharField(default='tapas', max_length=30)

    def __str__(self):
        return self.nombre

class productos_pedidos(models.Model):
    identificador_cuenta = models.FloatField()
    identificador_pedido = models.IntegerField()
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    num = models.IntegerField()
    activa = models.BooleanField(default=False)     

class pedidos(models.Model):
    identificador_cuenta = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    fecha = models.DateTimeField(auto_now=True)
    activa = models.BooleanField(default=False)

class llamadas(models.Model):
    identificador_mesa= models.IntegerField(default=0)
    hora = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=False)

class cuentas(models.Model):
    identificador_mesa = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    activa = models.BooleanField(default=False)