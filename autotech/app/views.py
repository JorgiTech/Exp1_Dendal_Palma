from django.shortcuts import render
from .models import Producto


# Create your views here.
def index(request):
    return render(request,'app/index.html')

def nosotros(request):
    return render(request,'app/nosotros.html')

def galeria(request):
    return render(request,'app/galeria.html')

def api(request):
    return render(request,'app/api.html')

def formulario(request):
    return render(request,'app/formulario.html')

def productos(request):
    pro=Producto.objects.all()
    return render(request,'app/productos.html',{'pro':pro})
