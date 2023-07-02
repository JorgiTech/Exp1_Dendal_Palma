from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'app/index.html')

def nosotros(request):
    return render(request,'app/nosotros.html')

def galeria(request):
    return render(request,'app/galetia.html')

def api(request):
    return render(request,'app/api.html')

def formulario(request):
    return render(request,'app/formulario.html')