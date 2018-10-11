from datetime import date

class Pension:

    def __init__(self, fechaNac, sexo, semCotizadas, anosIns):

        # Datos Pensionado
        self.fechaNac = fechaNac
        self.sexo = sexo
        self.semCotizadas = semCotizadas
        self.anosIns = anosIns

        # Requerimientos para Pension
        self.semAcotizar = 750
        self.edadObjetivo = 60

    def cumple(self):
        pass

