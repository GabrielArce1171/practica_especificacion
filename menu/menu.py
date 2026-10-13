from ejercicios.ejercicio1_luz import leer_consumo, calcular_importe, mostrar_recibo
from ejercicios.ejercicio2_calificacion import LeerParciales, CalcularFinal, DeterminarEstado, MostrarResultado
from ejercicios.ejercicio3_compra import LeerSubtotal, CalcularDescuento, CalcularIVA, CalcularTotal, MostrarTicket
from ejercicios.ejercicio4_estacionamiento import leerMinutos, calcularCobro, mostrarCobro
from ejercicios.ejercicio5_renta import leerHoras, calcularRenta, mostrarRenta
from ejercicios.ejercicio6 import leerEdad, calcularPrecio, mostrarPrecio
from ejercicios.ejercicio7 import leerVelocidad, calcularMulta, mostrarMulta
 
 
def ejecutarEjercicio1(): 
    consumo = leer_consumo()
    importe = calcular_importe(consumo)
    mostrar_recibo(importe)
 
 
def ejecutarEjercicio2(): 
    calificacion1, calificacion2, calificacion3 = LeerParciales()
    calificacion_final = CalcularFinal(calificacion1, calificacion2, calificacion3)
    estado = DeterminarEstado(calificacion1, calificacion2, calificacion3, calificacion_final)
    MostrarResultado(estado, calificacion_final)
 
 
def ejecutarEjercicio3(): 
    monto_compra = LeerSubtotal()
    descuento = CalcularDescuento(monto_compra)
    subtotal = monto_compra - descuento
    iva = CalcularIVA(subtotal)
    total = CalcularTotal(subtotal, iva)
    MostrarTicket(subtotal, descuento, iva, total)
 
 
def ejecutarEjercicio4(): 
    minutos = leerMinutos()
    cobro = calcularCobro(minutos)
    mostrarCobro(cobro)
 

def ejecutarEjercicio5(): 
    horas_renta = leerHoras()
    importe = calcularRenta(horas_renta)
    mostrarRenta(importe)


def ejecutarEjercicio6(): 
    edad = leerEdad()
    precio = calcularPrecio(edad)
    mostrarPrecio(precio)


def ejecutarEjercicio7(): 
    velocidad = leerVelocidad()
    multa = calcularMulta(velocidad)
    mostrarMulta(multa)
 
def mostrarMenu(): 
    print() 
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Recibo de luz") 
    print("2. Calificación final") 
    print("3. Total de compra") 
    print("4. Estacionamiento") 
    print("0. Salir") 
 
 
def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion == "3": 
            ejecutarEjercicio3() 
        elif opcion == "4": 
            ejecutarEjercicio4() 
        elif opcion != "0": 
            print("Opción no válida.") 