productos = []  

try:
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
except FileNotFoundError:
    print("El archivo productos.txt no existe. Se creará automáticamente.")

if productos:
    print("Productos cargados desde el archivo:\n")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
else:
    print("No hay productos cargados.")
