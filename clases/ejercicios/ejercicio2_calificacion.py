class Calificacion(object):
    def __init__(self):
        self.calificacion1 = 0
        self.calificacion2 = 0
        self.calificacion3 = 0
    
    def LeerParciales(self):
        self.calificacion1 = float(input("Ingrese la calificación del primer parcial: "))
        self.calificacion2 = float(input("Ingrese la calificación del segundo parcial: "))
        self.calificacion3 = float(input("Ingrese la calificación del tercer parcial: "))
        return self.calificacion1, self.calificacion2, self.calificacion3

    def CalcularPromedio(self):
        return (self.calificacion1 * 0.3) + (self.calificacion2 * 0.3) + (self.calificacion3 * 0.4)

    def MostrarResultado(self):
        print("Calificaciones:")
        print("Primer parcial:", self.calificacion1)
        print("Segundo parcial:", self.calificacion2)
        print("Tercer parcial:", self.calificacion3)
        print("Promedio:", self.CalcularPromedio())
