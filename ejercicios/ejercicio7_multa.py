''' 
En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa es de $500. Si se excede 
por más de 20 km/h, la multa es de $1,000. Se necesita mostrar la multa a partir de la velocidad del 
vehículo. 
''' 
# PROBLEMA 
# Calcular la multa a partir de la velocidad del vehículo.

# ENTRADAS 
# velocidad del vehículo

# SALIDAS 
# Importe de la multa

# REGLAS Y SUPUESTOS 
# - Todo exceso de velocidad es sancionado con una multa.
# - La multa es de $500 si se excede hasta por 20 km/h.
# - La multa es de $1,000 si se excede por más de 20 km/h.

# ALGORITMO 
# 1. Leer la velocidad del vehículo.
# 2. Calcular la multa según la velocidad del vehículo. velocuidad <= 60 -> multa = 0; 60 < velocidad <= 80 -> multa = 500; velocidad > 80 -> multa = 1000.
# 3. Mostrar la multa a pagar.

# CASOS DE PRUEBA
#  50, 60, 61, 80 y 81 km/h -> $0.00, $0.00, $500.00, $1,000.00 y $1,000.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerVelocidad
# calcularMulta
# mostrarMulta

# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def leerVelocidad():
    velocidad = float(input("Ingrese la velocidad del vehículo (km/h): "))
    return velocidad

def calcularMulta(velocidad):
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000
    return multa

def mostrarMulta(multa):
    print(f"La multa a pagar es: ${multa:.2f}")
