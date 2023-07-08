from django.db import models

# Create your models here.
class Producto(models.Model):
    id=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50)
    valor=models.IntegerField()
