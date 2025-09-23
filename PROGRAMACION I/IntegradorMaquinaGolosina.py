# lista de productos , codigo , productos, stock
golosinas = (
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 7],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10],
)
# Diccionario "Empleados" , legajo + nombre
Empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia",
}

# Codificamos la Tupla "clavesTecnico"
clavesTecnico = ("admin", "CCCDDD", "2020")

# Variable "golosinasPedidas". inicializamos en 0 y Guardamos en el historial

golosinasPedidas = []

# Mostramos el historial de pedidos
for pedido in golosinasPedidas:
    print(
        f"Código Golosina: {pedido[0]}, Denominación Golosina: {pedido[1]}, Cantidad total pedida: {pedido[2]}"
    )


# Menu Interactivo
def mostrar_menu():
    print("\n--- Menú Máquina de Golosinas ---")
    print("1. Pedir golosina")
    print("2. Mostrar golosinas")
    print("3. Rellenar golosinas")
    print("4. Apagar maquina")


# Funciones
def pedir_golosina():
    legajo = int(input("Ingrese su legajo: "))

    if legajo not in Empleados:
        print("Usted no es un empleado de la empresa.")
        return

    print(f"Bienvenido {Empleados[legajo]}")

    while True:
        print("\nGolosinas disponibles:")
        for g in golosinas:
            print(f"Código: {g[0]}, Golosina: {g[1]}, Stock: {g[2]}")

        entrada = input(
            "Ingrese el código de la golosina o 'salir' para volver al menú: "
        ).lower()
        if entrada == "salir":
            break

        if not entrada.isdigit():
            print("Código inválido. Intente nuevamente.")
            continue

        codigo_golosina = int(entrada)
        encontrada = False

        for g in golosinas:
            if g[0] == codigo_golosina:
                encontrada = True
                if g[2] > 0:
                    g[2] -= 1
                    registrada = False
                    for pedido in golosinasPedidas:
                        if pedido[0] == g[0]:
                            pedido[2] += 1
                            registrada = True
                            break
                    if not registrada:
                        golosinasPedidas.append([g[0], g[1], 1])

                    print(f"Se ha entregado 1 {g[1]}.")
                else:
                    print(
                        f"Lo sentimos la golosina {g[1]} no se encuentra disponible, seleccione otra golosina o ingrese 'salir'."
                    )
                break

        if not encontrada:
            print("Código de golosina no válido.")


def mostrar_golosinas():
    print("\n--- Golosinas ---")
    for g in golosinas:
        print(f"Código: {g[0]}, Golosina: {g[1]}, Stock: {g[2]}")


def rellenar_golosinas():
    print("\n--- Rellenar golosinas ---")
    print(
        "Para autorizar la recarga, ingrese las 3 palabras de la clave de técnico en orden."
    )

    # Pedimos las 3 claves en orden
    clave1 = input("Ingrese la primera palabra: ")
    clave2 = input("Ingrese la segunda palabra: ")
    clave3 = input("Ingrese la tercera palabra: ")

    # Validamos la tupla clavesTecnico
    if (clave1, clave2, clave3) != clavesTecnico:
        print("No tiene permiso para ejecutar la función de recarga.")
        return  # Regresamos al menú

    print("Clave correcta. Puede recargar golosinas.")

    # Pedir código de la golosina a recargar
    entrada = input("Ingrese el código de la golosina que desea recargar: ")
    if not entrada.isdigit():
        print("Código inválido.")
        return
    codigo_golosina = int(entrada)

    # Buscamos la golosina
    encontrada = False
    for g in golosinas:
        if g[0] == codigo_golosina:
            encontrada = True
            while True:
                try:
                    cantidad = int(
                        input(f"Ingrese la cantidad a recargar para {g[1]}: ")
                    )
                    if cantidad <= 0:
                        print("Debe ingresar una cantidad mayor a cero.")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar un número entero.")

            g[2] += cantidad
            print(
                f"Se ha recargado {cantidad} unidades de {g[1]}. Stock actual: {g[2]}"
            )
            break

    if not encontrada:
        print("Código de golosina no válido.")


def apagar_maquina():
    print("\n--- Apagando la máquina ---")

    if golosinasPedidas:
        print("\nHistorial de golosinas pedidas:")
        total_pedidas = 0
        for pedido in golosinasPedidas:
            print(f"Código: {pedido[0]}, Golosina: {pedido[1]}, Cantidad: {pedido[2]}")
            total_pedidas += pedido[2]
        print(f"\nTotal de golosinas pedidas: {total_pedidas}")
    else:
        print("No se registraron pedidos durante la ejecución.")

    print("La máquina se apagó correctamente.")


def mostrar_menu():
    print("\n--- Menú Máquina de Golosinas ---")
    print("1. Pedir golosina")
    print("2. Mostrar golosinas")
    print("3. Rellenar golosinas")
    print("4. Apagar maquina")


# --- Programa principal ---
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            pedir_golosina()
        case "2":
            mostrar_golosinas()
        case "3":
            rellenar_golosinas()
        case "4":
            apagar_maquina()
            break
        case _:
            print("Opción no válida. Intente de nuevo.")
