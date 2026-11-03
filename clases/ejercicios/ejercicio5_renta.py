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

#Clase
#Nombre: Renta
#Responsabilidad: Calcular el importe a cobrar por la renta de bicicletas según las horas de renta.

#Atributos
# - horas_renta: float
# - importe: float

#Contrato de clase
# class Renta:
#     def __init__(self, horas_renta: float):
#         self.horas_renta = horas_renta
#         self.importe = 0.0

# ALGORITMO
# 1. Leer horas_renta
# 2. Calcular importe = horas_renta * 30
# 3. Si horas_renta >= 3:
#       importe = importe * 0.85
# 4. importe = max(0, importe)
# 5. Redondear importe a 2 decimales

class Renta:
    def __init__(self):
        self.horas_renta = 0
        self.importe = 0.0

    def leer_horas(self):
        self.horas_renta = float(input("Ingrese el número de horas de renta: "))

    def calcular_importe(self):
        self.importe = self.horas_renta * 30
        if self.horas_renta >= 3:
            self.importe *= 0.85
        self.importe = max(0, round(self.importe, 2))

    def mostrar_importe(self):
        print("El importe a pagar por la renta de bicicletas es:", self.importe)