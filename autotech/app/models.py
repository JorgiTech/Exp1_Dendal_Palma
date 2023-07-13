from django.db import models

# Create your models here.
class Producto(models.Model):
    id=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50)
    valor=models.IntegerField()


#class ItemCarrito(models.Model):
 #   producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  #  cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'