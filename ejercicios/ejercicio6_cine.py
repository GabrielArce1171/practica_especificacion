''' 
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años o más pagan la mitad. 
Se necesita mostrar el precio del boleto según la edad. 
''' 
# PROBLEMA 
# Calcular el precio del boleto a partir de la edad del cliente.

# ENTRADAS 
# Edad del cliente

# SALIDAS 
# Precio del boleto

# REGLAS Y SUPUESTOS 
# - Tarifas: $80 por boleto.
# - Descuento: 50% para niños de hasta 12 años y adultos de 60 años o más.

# ALGORITMO 
# 1. Leer la edad del cliente.
# 2. Calcular el precio del boleto.
# 3. Si edad <= 12 o edad >= 60, aplicar descuento del 50%.
# 4. Mostrar el precio del boleto.

# CASOS DE PRUEBA
# 8, 12, 13, 59 y 60 años -> $40.00, $40.00, $80.00, $80.00 y $40.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerEdad -> lee la edad del cliente
# calcularPrecio -> calcula el precio del boleto según la edad del cliente
# mostrarPrecio -> muestra el precio del boleto

# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def leerEdad():
    edad = int(input("Ingrese la edad del cliente: "))
    return edad

def calcularPrecio(edad):
    precio = 80
    if edad <= 12 or edad >= 60:
        precio *= 0.5
    return precio

def mostrarPrecio(precio):
    print(f"El precio del boleto es: ${precio:.2f}")
