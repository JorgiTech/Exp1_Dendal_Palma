from django.shortcuts import render


# Create your views here.

def FORMULARIO(request):
    return render(request, 'app/FORMULARIO.html')
def GALERIA(request):
    return render(request, 'app/GALERIA.html')
def HOME(request):
    return render(request, 'app/HOME.html')
def API(request):
    return render(request, 'app/API.html')
def NOSOTROS(request):
    return render(request, 'app/NOSOTROS.html')


