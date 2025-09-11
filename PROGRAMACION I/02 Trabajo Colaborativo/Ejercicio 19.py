# Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un
# atributo de nombre operación.
# Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
# sumarNumeros()
# restarNumeros()
# multiplicarNumeros()
# dividirNumeros()
# El quinto método será el siguiente:
# aplicarOperacion(operacion){
# …………………..

# Cree una clase Calculo que contenga un método main, donde cree una instancia de la
# clase OperacionMatematica, asigne 2 valores para las variables de la instancia y
# ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “
# ”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las
# operaciones.


# Creamos la clase que realiza las operaciones matemáticas
class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"

    # Quinto Metodo
    def aplicarOperacion(self, operacion):
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"


# Clase calculo que contiene un metodo main , crea una instacia de la clase
# OperacionMatematica, le asignamos valor y luego ejecutamos la operacion teniendo
# en cuenta el ordenamiento de los parametros
class Calculo:
    @staticmethod
    def main():
        # Creamos una instancia con dos números
        operacion = OperacionMatematica(10, 5)

        # Mostramos los valores asignados
        print("Valores asignados:")
        print("---------------------------")
        print("Valor 1:", operacion.valor1)
        print("Valor 2:", operacion.valor2)
        print("---------------------------")
        # Aplicamos las operaciones y mostramos resultados
        print("Suma: ", operacion.aplicarOperacion("+"))
        print("Resta:", operacion.aplicarOperacion("-"))
        print("Multiplicación:", operacion.aplicarOperacion("*"))
        print("División:", operacion.aplicarOperacion("/"))


# Ejecutamos el programa
Calculo.main()
