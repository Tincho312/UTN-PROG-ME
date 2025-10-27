with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
