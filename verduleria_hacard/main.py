import os
from creaproductosjson import generar_productos_json
from modulo2 import ejecutar_menu

# Verificar si el archivo ya existe
ruta_json = os.path.join(os.path.dirname(__file__), "verduras.json")
if not os.path.exists(ruta_json):
    print(" Arc1hivo verduras.json no encontrado. Generando...")
    generar_productos_json()

# Ejecutar la app
if __name__ == "__main__":
    base = {}
    ejecutar_menu(base)
