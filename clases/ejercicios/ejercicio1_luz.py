class Luz(object):
    def __init__(self):
        self.costo_hora = 0
        self.consumo = 0

    def leer_consumo(self):
        self.consumo = float(input("Ingrese el consumo del mes en kWh: "))
        if self.consumo < 0:
            self.consumo = 0
        return self.consumo

    def calcular_costo(self):
        return self.costo_hora * self.consumo

    def mostrar_resultado(self):
        print("Consumo total:", self.consumo)
        print("Costo total:", self.calcular_costo())