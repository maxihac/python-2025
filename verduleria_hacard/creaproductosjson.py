
import json
import os
from modulo1 import Producto

def generar_productos_json():
    productos = [
        Producto("Manzana", "Fruta roja, dulce y crocante", 850, 50),
        Producto("Banana", "Fruta tropical rica en potasio", 780, 40),
        Producto("Tomate", "Ideal para ensaladas y salsas", 620, 60),
        Producto("Lechuga", "Hojas verdes frescas para ensalada", 430, 35),
        Producto("Papa", "Tubérculo versátil para cocinar", 520, 100),
        Producto("Zanahoria", "Raíz naranja rica en vitamina A", 490, 80),
        Producto("Cebolla", "Base aromática para muchas comidas", 550, 70),
        Producto("Pimiento", "Verdura colorida y sabrosa", 670, 45),
        Producto("Naranja", "Fruta cítrica rica en vitamina C", 800, 55),
        Producto("Acelga", "Hojas verdes para tartas y guisos", 400, 30)
    ]

    productos_dict = [p.to_dict() for p in productos]
    ruta_json = os.path.join(os.path.dirname(__file__), "verduras.json")

    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(productos_dict, archivo, indent=4, ensure_ascii=False)

    print("✅ Archivo verduras.json generado con éxito.")
