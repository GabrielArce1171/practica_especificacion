''' 
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes. 
''' 
# PROBLEMA 
# Calcular el importe del recibo de luz a partir del consumo del mes.
 
# ENTRADAS 
# costo_hora : float, kWh, número de kilovatios-hora consumidos en el mes.
# consumo : float, kWh, número de kilovatios-hora consumidos en el mes.
 
# SALIDAS 
# importe : float, $US, importe total a pagar.

# REGLAS Y SUPUESTOS 
# - Tarifas: $1.00 por kWh hasta 150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh.
# - Redondeo: se redondea a dos decimales.
# - Si el consumo es negativo, se considera como 0.

# ALGORITMO 
# 1. Leer consumo
# 2. Si consumo <= 150: 
#       importe = consumo * 1.00
# 3. En caso contrario:
#       importe = 150 * 1.00 + (consumo - 150) * 1.50
# 4. Mostrar importe

# CASOS DE PRUEBA
# 100, 150, 200, 280 y 300 kWh 

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py. 
 
# CONTRATO DE FUNCIONES 
# leer_consumo() -> float : lee el consumo del mes en kWh
# calcular_importe(consumo: float) -> float : calcula el importe del recibo
# mostrar_recibo(importe: float) -> None : muestra el recibo

# Implementa el algoritmo anterior utilizando las funciones del contrato. 
