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
    print("Productos cargados:\n")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
else:
    print("No hay productos cargados.")

nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").strip()

encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")
