''' 
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total. 
''' 
# PROBLEMA 
# Que se necesita calcular el total de una compra considerando descuentos e IVA.
 
# ENTRADAS 
# Monto de la compra
 
# SALIDAS 
# Subtotal, descuento, IVA y total de la compra. 
 
# REGLAS Y SUPUESTOS 
# Aplica descuento del 10% en compras de $1,000 o más y 20% en compras de $5,000 o más.
# Al subtotal ya con descuento se le agrega el 16% de IVA.
 
# ALGORITMO 
# 1. Leer monto_compra
# 2. Si monto_compra >= 5000:
#       descuento = monto_compra * 0.2
# 3. Si monto de compra es >= 1000:
#       descuento = monto_compra * 0.1
# 4. subtotal = monto_compra - descuento
# 5. IVA = subtotal * 0.16
# 6. total = subtotal + IVA
# 7. Mostrar subtotal, descuento, IVA y total

# CASOS DE PRUEBA
# $500 -> No hay descuento, subtotal = $500, IVA = $80, total = $580
# $900 -> No hay descuento , subtotal = $900, IVA = $144, total = $1,044
# $1,000 -> Descuento del 10%, subtotal = $900, IVA = $144, total = $1,044
# $5,000 -> Descuento del 20%, subtotal = $4,000, IVA = $640, total = $4,640

# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# LeerSubtotal
# CalcularDescuento
# CalcularIVA
# CalcularTotal 
# MostrarTicket  
 
# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def LeerSubtotal():
    monto_compra = float(input("Ingrese el monto de la compra: "))
    return monto_compra

def CalcularDescuento(monto_compra):
    if monto_compra >= 5000:
        return monto_compra * 0.2
    elif monto_compra >= 1000:
        return monto_compra * 0.1
    return 0

def CalcularIVA(subtotal):
    return subtotal * 0.16

def CalcularTotal(subtotal, iva):
    return subtotal + iva

def MostrarTicket(subtotal, descuento, iva, total):
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"IVA: ${iva}")
    print(f"Total: ${total}")