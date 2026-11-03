from clases.ejemplo.calculadora import Calculadora
from clases.ejercicios.ejercicio1_luz import Luz
from clases.ejercicios.ejercicio2_calificacion import Calificacion
from clases.ejercicios.ejercicio3_compra import Compra
from clases.ejercicios.ejercicio4_estacionamiento import Estacionamiento
from clases.ejercicios.ejercicio5_renta import Renta

class Menu(object):
    def __init__(self):
        self.opcion = 0
    
    def mostrar_menu(self):
        print() 
        print("Ejemplo: programación aplicada a objetos") 
        print("1. Calculadora") 
        print("2. Ejercicio 1: Cálculo de costo de luz")
        print("3. Ejercicio 2: Cálculo de calificaciones")
        print("4. Ejercicio 3: Cálculo de compra con descuento e IVA")
        print("5. Ejercicio 4: Cálculo de estacionamiento")
        print("6. Ejercicio 5: Cálculo de renta de bicicletas")
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

            elif self.opcion == "4":
                Venta = Compra()
                Venta.leer_datos()
                Venta.calcular_descuento()
                Venta.calcular_subtotal()
                Venta.calcular_iva()
                Venta.calcular_total()
                Venta.mostrar_ticket()

            elif self.opcion == "5":
                CobroEstacionamiento = Estacionamiento()
                CobroEstacionamiento.leer_tiempo()
                CobroEstacionamiento.calcular_importe()
                CobroEstacionamiento.mostrar_ticket()

            elif self.opcion == "6":
                RentaBici = Renta()
                RentaBici.leer_horas()
                RentaBici.calcular_importe()
                RentaBici.mostrar_importe()

            else:
                print("Opción inválida. Intente de nuevo.")
    