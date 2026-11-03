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

#Clase
#Nombre: Compra
#Responsabilidad: Calcular el total de una compra considerando descuentos e IVA.

#Atributos
# - monto: float
# - subtotal: float
# - descuento: float
# - iva: float
# - total: float

#Contrato de clase
# class Compra:
#     def __init__(self, monto: float):
#         self.monto = monto
#         self.subtotal = 0.0
#         self.descuento = 0.0
#         self.iva = 0.0
#         self.total = 0.0

# ALGORITMO
# 1. Leer monto_compra
# 2. Si monto_compra >= 5000:
#       descuento = monto_compra * 0.2
# 3. Si monto de compra es >= 1000:
#       descuento = monto_compra * 0.1
# 4. subtotal = monto_compra - descuento
# 5. iva = subtotal * 0.16
# 6. total = subtotal + iva

class Compra:
    def __init__(self, monto: float):
        self.monto = monto
        self.subtotal = 0.0
        self.descuento = 0.0
        self.iva = 0.0
        self.total = 0.0

    def calcular_descuento(self):
        if self.monto >= 5000:
            self.descuento = self.monto * 0.2
        elif self.monto >= 1000:
            self.descuento = self.monto * 0.1

    def calcular_subtotal(self):
        self.subtotal = self.monto - self.descuento

    def calcular_iva(self):
        self.iva = self.subtotal * 0.16

    def calcular_total(self):
        self.total = self.subtotal + self.iva

    def mostrar_ticket(self):
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Descuento: ${self.descuento:.2f}")
        print(f"IVA: ${self.iva:.2f}")
        print(f"Total: ${self.total:.2f}")