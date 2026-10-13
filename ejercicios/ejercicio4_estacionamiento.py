''' 
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción. 
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y 
muestra el importe a cobrar.  
''' 
# PROBLEMA 
# Calcular el importe a cobrar por el estacionamiento según el tiempo de estancia.
 
# ENTRADAS 
# Tiempo de estancia en minutos 
 
# SALIDAS 
# Importe a cobrar por el estacionamiento
 
# REGLAS Y SUPUESTOS 
# El cobro máximo es de $150.
# La primera hora se cobra $20 y cada hora adicional o fracción se cobra $15.
 
# ALGORITMO 
# 1. Leer el tiempo de estancia en minutos.
# 2. Calcular el tiempo de estancia en horas, redondeando hacia arriba.
# 3. Calcular el importe a cobrar según las reglas del estacionamiento.
# 4. Mostrar el importe a cobrar.
 
# CASOS DE PRUEBA 
# 45 -> 20
# 60 -> 20
# 61 -> 35
# 150 -> 150
# 600 -> 150

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerMinutos -> Lee los minutos de estancia y los devuelve como un número entero.
# calcularCobro -> Calcula el importe a cobrar según el tiempo de estancia en minutos y devuelve el importe como un número entero.
# mostrarCobro -> Muestra el imprte a pagar por el estacionamiento.
 
# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def leerMinutos():
    minutos = int(input("Ingrese el tiempo de estancia en minutos: "))
    return minutos

def calcularCobro(minutos):
    horas = (minutos + 59) // 60
    if horas == 1:
        return 20
    elif horas > 1:
        return min(20 + (horas - 1) * 15, 150)

def mostrarCobro(cobro):
    print("El importe a pagar por el estacionamiento es:", cobro)