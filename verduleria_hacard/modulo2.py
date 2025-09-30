import os
import json
from modulo1 import Cliente, Producto
base = {}

def usuario_nuevo(base):
    cliente = Cliente()
    cliente.agregar()  # Carga los datos desde input
    base[cliente.usuario] = cliente
    print("✅ Registro Ok")


def mostrar_base(base):
    print("\n--- BASE DE CLIENTES ---")
    if not base:
        print("No hay clientes registrados.")
        return
    for usuario, cliente in base.items():
        print(f"\nUsuario: {usuario}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Email: {cliente.email}")

def mostrar_productos(productos):
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto}")


def cargar_productos():
    try:
        ruta = os.path.join(os.path.dirname(__file__), "verduras.json")
        with open(ruta, "r", encoding="utf-8") as archivo:
            productos_data = json.load(archivo)
            productos = [Producto(**p) for p in productos_data]
            return productos
    except FileNotFoundError:
        print("⚠️ Archivo verduras.json no encontrado en la carpeta del script.")
        return []

def seleccionar_producto(productos):
    while True:
        opcion = input("Ingrese el número del producto que desea comprar (o 'f' para salir): ").lower()
        if opcion == "f":
            return None, 0
        elif opcion.isdigit() and 1 <= int(opcion) <= len(productos):
            seleccionado = productos[int(opcion) - 1]
            try:
                cantidad = int(input(f"Ingrese cantidad (max {seleccionado.stock}): "))
                if 0 < cantidad <= seleccionado.stock:
                    return seleccionado, cantidad
                else:
                    print(" Cantidad inválida.")
            except ValueError:
                print(" Entrada inválida.")
        else:
            print("Opcion inválida.")
def procesar_compra(cliente, carrito):
    print("\n--- CONFIRMACIoN DE COMPRA ---")
    total = 0
    for producto, cantidad in carrito:
        cliente.comprar(producto, cantidad)
        total += producto.precio * cantidad
    print(f"Compra confirada. Total: ${total}")
    print("Gracias por comprar")


def login(base):
    print("--- LOGIN ---")
    usuario = input("Usuario: ")
    if usuario in base:
        cliente = base[usuario]
        contraseña = input("Contraseña: ")
        if contraseña == cliente.contraseña:
            print(f"Login exitoso. Bienvenido {cliente.nombre}")
            productos = cargar_productos()
            carrito = []

            while True:
                mostrar_productos(productos)
                producto, cantidad = seleccionar_producto(productos)
                if producto is None:
                    print("Cancelaste la compra.")
                    break
                carrito.append((producto, cantidad))
                seguir = input("¿Desea comprar otro producto? (s/n): ").lower()
                if seguir != "s":
                    procesar_compra(cliente, carrito)
                    break
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no registrado.")


# Menú principal
def ejecutar_menu(base):
    while True:
        print("\n<-- MENÚ PRINCIPAL, SELECCIONA UNA OPCIÓN --->")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Login")
        print("4. Salir")
        try:
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                usuario_nuevo(base)
            elif opcion == "2":
                mostrar_base(base)
            elif opcion == "3":
                login(base)
            elif opcion == "4":
                print("Saliste del programa.")
                break
            else:
                print("Opción inválida. Intente otra vez.")
        except KeyboardInterrupt:
            print("\nPresionaste Ctrl + C. Cerrando programa.")
            break
        except Exception as e:
            print(f"Error: {e}")
