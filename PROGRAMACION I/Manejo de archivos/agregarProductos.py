try:
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        print("Productos actuales:\n")
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
except FileNotFoundError:
    print("El archivo productos.txt no existe. Se creará automáticamente.")

print("\nIngrese un nuevo producto:")
nombre = input("Nombre: ").strip()
precio = input("Precio: ").strip()
cantidad = input("Cantidad: ").strip()

with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\nProducto agregado correctamente.")
