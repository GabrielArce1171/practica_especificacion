''' 
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. Se 
necesita mostrar el importe a pagar según las horas de renta. 
''' 
# PROBLEMA 
# Calcular el importe del recibo de renta a partir de las horas de renta.

# ENTRADAS 
# horas_renta : float, número de horas de renta.

# SALIDAS 
# importe : float, $US, importe total a pagar.

# REGLAS Y SUPUESTOS 
# - Tarifas: $30 por hora.
# - Descuento: 15% si se rentan 3 horas o más.
# - Redondeo: se redondea a dos decimales.
# - Si el consumo es negativo, se considera como 0.

# ALGORITMO 
# 1. Leer el número de horas de renta.
# 2. Calcular el importe a pagar.

# CASOS DE PRUEBA
# 1 hora -> $30.00
# 2 horas -> $60.00
# 3 horas -> $76.50
# 4 horas -> $97.50

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leerHoras -> lee las horas de renta
# calcularRenta -> calcula el importe a pagar según las horas de renta
# mostrarRenta -> muestra el importe a pagar

# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def leerHoras():
    horas_renta = float(input("Ingrese el número de horas de renta: "))
    if horas_renta < 0:
        horas_renta = 0
    return horas_renta

def calcularRenta(horas_renta):
    importe = horas_renta * 30
    if horas_renta >= 3:
        importe *= 0.85
    return round(importe, 2)

def mostrarRenta(importe):
    print("El importe a pagar por la renta de bicicletas es:", importe)