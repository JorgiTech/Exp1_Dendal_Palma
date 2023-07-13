
from django.shortcuts import redirect,render,get_object_or_404, HttpResponse

from .Carrito import Carrito
from .context_processor import total_carrito


# from . import Carrito
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
#agregar xD
def formulario(request):
    return render(request,'app/formulario.html')

def productos(request):
    pro=Producto.objects.all()
    return render(request,'app/productos.html',{'pro':pro})

def agregar(request):
    return render(request,'app/agregar.html')




def agregarsave(request):
    if 'nombre' in request.POST:
        x = request.POST['id']
        y = request.POST['nombre']
        z = request.POST['valor']
        pro = Producto(id=x, nombre=y, valor=z)
        pro.save()
        return redirect("/productos/")
    else:
        return redirect("/productos/")



def eliminar(request, id):
    pro=Producto.objects.get(id=id)
    pro.delete()
    return redirect("/productos/")

def actualizar(request, id):
    pro = Producto.objects.get(id=id)
    return render(request, 'app/actualizar.html', {'pro': pro})

    
    
def actualizarsave(request, id):
    if request.method == 'POST':
        pro = get_object_or_404(Producto, id=id)
        pro.nombre = request.POST['nombre']
        pro.valor = request.POST['valor']
        pro.save()
        return redirect("/productos/")
    else:
        return redirect("/productos/")


def carrito(request):
    productos = Producto.objects.all()
    return render(request, "app/carrito.html", {'productos': productos, **total_carrito(request)})




def add(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.add(producto)
    return redirect("/carrito/")

def delete(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.delete(producto)
    return redirect("/carrito/")

def minus(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.minus(producto)
    return redirect("/carrito/")

def clean(request):
    carrito = Carrito(request)
    carrito.clean()
    return redirect("/carrito/")