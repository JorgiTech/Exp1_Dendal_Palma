class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def add(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.valor,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.valor
        self.save_carrito()

    def save_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def delete(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save_carrito()

    def minus(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.valor
            if self.carrito[id]["cantidad"] <= 0: self.delete(producto)
            self.save_carrito()

    def clean(self):
        self.session["carrito"] = {}
        self.session.modified = True