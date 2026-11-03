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

#Clase
#Nombre: Estacionamiento
#Responsabilidad: Calcular el importe a cobrar por el estacionamiento según el tiempo de estancia.

#Atributos
# - tiempo_estancia: float
# - importe: float

#Contrato de clase
# class Estacionamiento:
#     def __init__(self, tiempo_estancia: float):
#         self.tiempo_estancia = tiempo_estancia
#         self.importe = 0.0

# ALGORITMO
# 1. Leer tiempo_estancia
# 2. Calcular horas = tiempo_estancia / 60
# 3. Si horas <= 1:
#       importe = 20
# 4. Si horas > 1:
#       importe = 20 + (horas - 1) * 15
# 5. Si importe > 150:
#       importe = 150

class Estacionamiento:
    def __init__(self):
        self.tiempo_estancia = 0
        self.importe = 0.0
    
    def leer_tiempo(self):
        self.tiempo_estancia = float(input("Ingrese el tiempo de estancia en minutos: "))

    def calcular_importe(self):
        horas = (self.tiempo_estancia + 59) // 60  # Redondear hacia arriba
        if horas <= 1:
            self.importe = 20
        else:
            self.importe = 20 + (horas - 1) * 15
        if self.importe > 150:
            self.importe = 150

    def mostrar_ticket(self):
        print(f"Tiempo de estancia: {self.tiempo_estancia} minutos")
        print(f"Importe a cobrar: ${self.importe:.2f}")