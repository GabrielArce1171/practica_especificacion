''' 
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó.
''' 
# PROBLEMA 
# se necesita calcular la calificación final de un alumno a partir de las calificaciones de tres parciales y determinar si aprobó o no la materia.
 
# ENTRADAS 
# Calificacion1 : float, 0-100, calificación del primer parcial.
# Calificacion2 : float, 0-100, calificación del segundo parcial. 
# Calificacion3 : float, 0-100, calificación del tercer parcial.

# SALIDAS 
# Decision : string, "Aprobado" o "Reprobado", según corresponda.
# CalificacionFinal : float, calificación final del alumno, redondeada a un decimal. 
 
# REGLAS Y SUPUESTOS 
# El mínimo aprobar la materia es 70.
# El primer parcial vale 30% de la calificación final, el segundo parcial vale 30% y el tercer parcial vale 40%.
 
# ALGORITMO 
# 1. Leer Calificacion1, Calificacion2, Calificacion3
# 2. Si el conjunto de la Calificacion1 < 50 , Calificacion2 < 50 y Calificacion3 < 50: 
#       resultado = "Reprobado"
# 3. En caso contrario: 
#       resultado = "Aprobado"
# 4. Mostrar resultado

# CASOS DE PRUEBA 
# Caso de prueba 1: (80, 70, 90) -> Aprobado
# Caso de prueba 2: (70, 70, 70) -> Aprobado
# Caso de prueba 3: (100, 100, 40) -> Reprobado
# Caso de prueba 4: (69, 70, 70) -> Reprobado
 
# RESTRICCIONES PARA EL AGENTE 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# LeerParciales
# CalcularFinal 
# DeterminarEstado
# MostrarResultado 
 
# Implementa el algoritmo anterior utilizando las funciones del contrato. 

def LeerParciales():
    Calificacion1 = float(input("Ingrese la calificación del primer parcial: "))
    Calificacion2 = float(input("Ingrese la calificación del segundo parcial: "))
    Calificacion3 = float(input("Ingrese la calificación del tercer parcial: "))
    return Calificacion1, Calificacion2, Calificacion3

def CalcularFinal(Calificacion1, Calificacion2, Calificacion3):
    return round((Calificacion1 * 0.3) + (Calificacion2 * 0.3) + (Calificacion3 * 0.4), 1)

def DeterminarEstado(Calificacion1, Calificacion2, Calificacion3, CalificacionFinal):
    if Calificacion1 < 50 or Calificacion2 < 50 or Calificacion3 < 50:
        return "Reprobado"
    elif CalificacionFinal >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

def MostrarResultado(Estado, CalificacionFinal):
    print(f"Calificación final: {CalificacionFinal}")
    print(f"Estado: {Estado}")