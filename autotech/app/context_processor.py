from django.http import HttpResponse

def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        carrito = request.session.get('carrito', {})
        for key, value in carrito.items():
            total += int(value['acumulado'])
    return {'total_carrito': total}
