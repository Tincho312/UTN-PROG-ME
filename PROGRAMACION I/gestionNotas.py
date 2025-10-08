# Diccionario de alumnos
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales",
}
# Materias base: [Materia, Nota1, Nota2, NotaFinal]
materias_base = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografia", 0, 0, 0],
    ["Matematicas", 0, 0, 0],
    ["Fisica", 0, 0, 0],
]
# Lista de promedios finales: [Alumno, PromedioGeneral]
notasFinales = [
    ["Rodolfo Fernandez", 0],
    ["Luis Gomez", 0],
    ["Andrea Pereira", 0],
    ["Juan Cruz Gonzales", 0],
]


# Funciones
def pedir_nota(materia, nro):
    nota = float(input(f"  Nota {nro} ({materia}): "))
    while nota < 0 or nota > 10:
        nota = float(input(" Ingrese un valor entre 0 y 10: "))
    return nota


def cargar_materias(nombre):
    print(f"\n· Alumno: {nombre} ·")
    materias = [fila[:] for fila in materias_base]

    for m in materias:
        print(f"\nMateria: {m[0]}")
        n1 = pedir_nota(m[0], 1)
        n2 = pedir_nota(m[0], 2)
        m[1] = n1
        m[2] = n2
        m[3] = (n1 + n2) / 2
        print(f"  Nota Final: {m[3]:.2f}")
    return materias


def mostrar_materias(materias):
    print("\nMaterias cargadas:")
    for m in materias:
        print(f"{m[0]:<12}  {m[1]}  {m[2]}  Final: {m[3]:.2f}")


def promedio_general(materias):
    return sum(m[3] for m in materias) / len(materias)


def mejor_materia(materias):
    return max(materias, key=lambda x: x[3])


# Programa principal

for legajo, nombre in alumnos.items():
    materias_cargadas = cargar_materias(nombre)
    mostrar_materias(materias_cargadas)

    mejor = mejor_materia(materias_cargadas)
    print(f"\n Mejor materia: {mejor[0]} con {mejor[3]:.2f}")

    promedio = promedio_general(materias_cargadas)
    print(f" Promedio general de {nombre}: {promedio:.2f}")

    # Guardar en notasFinales
    for fila in notasFinales:
        if fila[0] == nombre:
            fila[1] = promedio

# Mejor alumno
mejor_alumno = max(notasFinales, key=lambda x: x[1])
print("\n· Promedios Finales ·")
for fila in notasFinales:
    print(f"{fila[0]}: {fila[1]:.2f}")

print(f"\n Mejor promedio: {mejor_alumno[0]} con {mejor_alumno[1]:.2f}")
