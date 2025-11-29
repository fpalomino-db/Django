from django.db import models

# Create your models here.
class mascota(models.Model):
    nombre = models.CharField(max_length= 64, null=True, blank=True)
    edad = models.IntegerField(null=True,blank=True)
    tipo = models.CharField(max_length= 32, null=True, blank=True)
    estado = models.CharField(max_length= 25, null=True, blank=True)