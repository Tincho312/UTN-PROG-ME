# Agregue a la clase los siguientes 4 métodos e implemente los mismos:
# sumarFracciones(Fraccion f1, Fraccion f2)
# restarFracciones(Fraccion f1, Fraccion f2)
# multiplicarFracciones(Fraccion f1, Fraccion f2)
# dividirFracciones(Fraccion f1, Fraccion f2)
# Todos los métodos deben retornar la fracción resultante de la operación.
# Cree una clase OperacionesFraccion que contenga un método main donde se solicite
# al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos
# Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos
# implementados anteriormente asignando el resultado a una nueva variable de tipo
# Fracción y mostrando por pantalla el resultado de las operaciones realizadas.


class Fraccion:
    # Validación para que el denominador no sea 0
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador

    # Función auxiliar para validar entrada numérica
    @staticmethod
    def pedir_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número entero.")

    # Mostramos la fracción
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    # Método para simplificar la fracción
    def simplificar(self):
        def mcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        divisor = mcd(abs(self.numerador), abs(self.denominador))
        self.numerador //= divisor
        self.denominador //= divisor

    # Operaciones: SUMA, RESTA, MULTIPLICACIÓN Y DIVISIÓN
    @staticmethod
    def sumar(f1, f2):
        num = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def restar(f1, f2):
        num = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def multiplicar(f1, f2):
        num = f1.numerador * f2.numerador
        den = f1.denominador * f2.denominador
        return Fraccion(num, den)

    @staticmethod
    def dividir(f1, f2):
        if f2.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con numerador 0.")
        num = f1.numerador * f2.denominador
        den = f1.denominador * f2.numerador
        return Fraccion(num, den)


# Clase OperacionesFraccion y método main
class OperacionesFraccion:
    @staticmethod
    def main():
        print("---------------------------------------------")
        print("Ingrese los valores de la primera fracción:")
        n1 = Fraccion.pedir_entero("Numerador 1: ")
        d1 = Fraccion.pedir_entero("Denominador 1: ")
        print("---------------------------------------------")
        print("\nIngrese los valores de la segunda fracción:")
        n2 = Fraccion.pedir_entero("Numerador 2: ")
        d2 = Fraccion.pedir_entero("Denominador 2: ")

        try:
            f1 = Fraccion(n1, d1)
            f2 = Fraccion(n2, d2)

            suma = Fraccion.sumar(f1, f2)
            # suma = f1.sumar(f2)

            resta = Fraccion.restar(f1, f2)
            multiplicacion = Fraccion.multiplicar(f1, f2)
            division = Fraccion.dividir(f1, f2)

            # Creamos copias para mostrar el resultado simplificado
            suma_simplificada = Fraccion(suma.numerador, suma.denominador)
            suma_simplificada.simplificar()

            resta_simplificada = Fraccion(resta.numerador, resta.denominador)
            resta_simplificada.simplificar()

            multiplicacion_simplificada = Fraccion(
                multiplicacion.numerador, multiplicacion.denominador
            )
            multiplicacion_simplificada.simplificar()

            division_simplificada = Fraccion(division.numerador, division.denominador)
            division_simplificada.simplificar()

            print("---------------------------------------------")
            print("\nResultados:")
            print(f"{f1} + {f2} = {suma} (simplificada: {suma_simplificada})")
            print(f"{f1} - {f2} = {resta} (simplificada: {resta_simplificada})")
            print(
                f"{f1} * {f2} = {multiplicacion} (simplificada: {multiplicacion_simplificada})"
            )
            print(f"{f1} / {f2} = {division} (simplificada: {division_simplificada})")

        except ValueError as e:
            print("Error:", e)


# Ejecutamos el programa
if __name__ == "__main__":
    OperacionesFraccion.main()
