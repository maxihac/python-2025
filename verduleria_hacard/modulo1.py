
class Cliente:
    def __init__(self, usuario="", contraseña="", nombre="", email=""):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.email = email
        self.historial_compras = []

    def __str__(self):
        return f"{self.nombre} ({self.usuario})"

    def agregar(self):
        print("\n--- REGISTRO DE CLIENTE ---")
        self.usuario = input("Usuario: ")
        self.contraseña = input("Contraseña: ")
        self.nombre = input("Nombre completo: ")
        self.email = input("Email: ")
        print("✅ Cliente registrado con éxito.")

    def comprar(self, producto, cantidad):
        if cantidad <= producto.stock:
            producto.stock -= cantidad
            self.historial_compras.append(f"{cantidad} x {producto.nombre}")
            print(f"🛒 Compra realizada: {cantidad} x {producto.nombre}")
        else:
            print(f"❌ Stock insuficiente para {producto.nombre}. Disponible: {producto.stock}")

    def mostrar_historial_compras(self):
        if not self.historial_compras:
            return "No hay compras registradas."
        return f"Compras: {', '.join(self.historial_compras)}"

    

class Producto:
    def __init__(self, nombre, descripcion, precio, stock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.stock} disponibles)"
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock
        }
    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


