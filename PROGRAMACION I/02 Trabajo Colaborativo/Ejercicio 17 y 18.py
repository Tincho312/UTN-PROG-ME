# 17- Cree una clase FuncionesPrograma y codifique una función estática getFechaString
# que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
# Ejemplo recibo 15/10/1900, la salida debe ser
# Quince de Octubre de mil novecientos.

# 18- En la clase FuncionesPrograma codifique una método getFechaDate estática que
# reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha de tipo
# date correspondiente.
# En la clase Principal creada en el punto anterior haga uso de la función getFechaDate.


from datetime import date


# Creamos la clase
class FuncionesPrograma:
    # staticmethod = no necesita un objeto de la clase para ser usado
    @staticmethod
    # Creamos nuestro metodo
    def getFechaString(fecha):
        # Listas para días y meses en palabras
        dias = [
            "Primero",
            "Dos",
            "Tres",
            "Cuatro",
            "Cinco",
            "Seis",
            "Siete",
            "Ocho",
            "Nueve",
            "Diez",
            "Once",
            "Doce",
            "Trece",
            "Catorce",
            "Quince",
            "Dieciséis",
            "Diecisiete",
            "Dieciocho",
            "Diecinueve",
            "Veinte",
            "Veintiuno",
            "Veintidós",
            "Veintitrés",
            "Veinticuatro",
            "Veinticinco",
            "Veintiséis",
            "Veintisiete",
            "Veintiocho",
            "Veintinueve",
            "Treinta",
            "Treinta y uno",
        ]
        meses = [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        ]

        # Separa la cadena a numero enteros dia , mes , años - luego divide la cadena x / , finalmente convierte cada parte a entero
        dia, mes, anio = map(int, fecha.split("/"))

        # Convierte la parte de miles del año en palabras
        # Resto guarda los números que quedan para convertir centenas, decenas y unidades
        if anio >= 2000:
            texto_anio = "dos mil"
            resto = anio - 2000
        else:
            texto_anio = "mil"
            resto = anio - 1000

        # Listas para convertir centenas, decenas y unidades del año en palabras
        centenas = [
            "",
            "cien",
            "doscientos",
            "trescientos",
            "cuatrocientos",
            "quinientos",
            "seiscientos",
            "setecientos",
            "ochocientos",
            "novecientos",
        ]
        decenas = [
            "",
            "diez",
            "veinte",
            "treinta",
            "cuarenta",
            "cincuenta",
            "sesenta",
            "setenta",
            "ochenta",
            "noventa",
        ]
        unidades = [
            "",
            "uno",
            "dos",
            "tres",
            "cuatro",
            "cinco",
            "seis",
            "siete",
            "ocho",
            "nueve",
        ]

        # Convierte la parte de centenas del año
        # resto // 100 obtiene la cantidad de centenas
        # resto %= 100 deja solo las decenas y unidades restantes
        if resto >= 100:
            texto_anio += " " + centenas[resto // 100]
            resto %= 100
        # Convierte las decenas y unidades restantes del año
        if resto >= 10:
            texto_anio += " " + decenas[resto // 10]
            resto %= 10
        if resto > 0:
            texto_anio += " " + unidades[resto]

        # Devuelve la fecha completa en palabras: "Quince de Octubre de mil novecientos".
        # strip() quita espacios extra al inicio o final.
        return f"{dias[dia-1]} de {meses[mes-1]} del {texto_anio.strip()}"

    # Método estático que recibe tres enteros: dia, mes y anio.
    # Retorna un objeto date de Python
    @staticmethod
    def getFechaDate(dia, mes, anio):
        return date(anio, mes, dia)


# Clase principal que tiene un método main para ejecutar el programa
class Principal:
    @staticmethod
    def main():
        # Pedimos al usuario el dia , mes , año y convertimos cada valor a entero
        dia = int(input("Ingresa el día: "))
        mes = int(input("Ingresa el mes: "))
        anio = int(input("Ingresa el año: "))

        # Usamos getFechaDate para crear el objeto date
        fecha_obj = FuncionesPrograma.getFechaDate(dia, mes, anio)
        # Mostramos el objeto
        print("La fecha de tipo date es:", fecha_obj)

        # Usamos getFechaString para obtener la fecha en palabras
        fecha_str = FuncionesPrograma.getFechaString(f"{dia:02d}/{mes:02d}/{anio}")
        # Imprimios la fecha en palabras
        print("La fecha en letras es:", fecha_str)


# Ejecutar programa
if __name__ == "__main__":
    Principal.main()
