# Listas paralelas
ordenes = []
horas = []


# Función para mostrar el menú
def mostrar_menu():
    print("\n=== Sistema de Gestión de Órdenes ===")
    print("1. Agregar nueva orden")
    print("2. Mostrar todas las órdenes")
    print("3. Buscar orden por código")
    print("4. Actualizar tiempo estimado")
    print("5. Eliminar orden")
    print("7. Ver sin estimación")
    print("8. Salir")


# Bucle principal
opcion = 0
while opcion != 8:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if opcion == 1:
        # Agregar nueva orden
        codigo = input("Ingrese el código de la orden (ej. ORD-001): ")
        if codigo in ordenes:
            print("El código ya existe.")
        else:
            try:
                tiempo = float(input("Ingrese el tiempo estimado en horas: "))
                ordenes.append(codigo)
                horas.append(tiempo)
                print(f"Orden {codigo} agregada con {tiempo} horas estimadas.")
            except ValueError:
                print("Tiempo inválido. Debe ser un número.")

    elif opcion == 2:
        # Mostrar todas las órdenes
        if not ordenes:
            print("No hay órdenes registradas.")
        else:
            print("\n")
            for i in range(len(ordenes)):
                print(f"{ordenes[i]} -> {horas[i]} horas")

    elif opcion == 3:
        # Buscar orden por código
        codigo = input("Ingrese el código de la orden a buscar: ")
        if codigo in ordenes:
            indice = ordenes.index(codigo)
            print(f"Orden {codigo} -> {horas[indice]} horas estimadas")
        else:
            print("Orden no encontrada.")

    elif opcion == 4:
        # Actualizar tiempo estimado
        codigo = input("Ingrese el código de la orden a actualizar: ")
        if codigo in ordenes:
            indice = ordenes.index(codigo)
            try:
                nuevo_tiempo = float(input(f"Ingrese nuevo tiempo para {codigo}: "))
                horas[indice] = nuevo_tiempo
                print(
                    f"Tiempo de la orden {codigo} actualizado a {nuevo_tiempo} horas."
                )
            except ValueError:
                print("Tiempo inválido. Debe ser un número.")
        else:
            print("Orden no encontrada.")

    elif opcion == 5:
        # Eliminar orden
        codigo = input("Ingrese el código de la orden a eliminar: ")
        if codigo in ordenes:
            indice = ordenes.index(codigo)
            ordenes.pop(indice)
            horas.pop(indice)
            print(f"Orden {codigo} eliminada.")
        else:
            print("Orden no encontrada.")

    elif opcion == 7:
        # Listar órdenes pendientes de diagnóstico (0 horas)
        pendientes = [ordenes[i] for i in range(len(ordenes)) if horas[i] == 0]
        if pendientes:
            print("\nÓrdenes pendientes de diagnóstico (0 horas):")
            for codigo in pendientes:
                print(f"- {codigo}")
        else:
            print("No hay órdenes pendientes de diagnóstico.")

    elif opcion == 8:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida. Intente nuevamente.")
