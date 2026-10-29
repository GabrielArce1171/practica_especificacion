from clases.ejemplo.calculadora import Calculadora
from clases.ejercicios.ejercicio1_luz import Luz
from clases.ejercicios.ejercicio2_calificacion import Calificacion

class Menu(object):
    def __init__(self):
        self.opcion = 0
    
    def mostrar_menu(self):
        print() 
        print("Ejemplo: programación aplicada a objetos") 
        print("1. Calculadora") 
        print("2. Ejercicio 1: Cálculo de costo de luz")
        print("3. Ejercicio 2: Cálculo de calificaciones")
        print("0. Salir")
    
    def menu(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")
            if self.opcion == "1":
                casio = Calculadora()
                casio.leerNumeros()
                casio.calcularSuma()
                casio.mostrarSuma()
            elif self.opcion == "2":
                CFE = Luz ()
                CFE.leer_consumo()
                CFE.calcular_costo()
                CFE.mostrar_resultado()
            elif self.opcion == "3":
                UNI = Calificacion()
                UNI.LeerParciales()
                UNI.CalcularPromedio()
                UNI.MostrarResultado()
            else:
                print("Opción inválida. Intente de nuevo.")
    