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
        return (self.calcularEdad() >= self.edadObjetivo and
                 self.semCotizadas >= self.semAcotizar)

    def calcularEdad(self):
        hoy = date.today()
        nac = self.fechaNac
        edad = hoy.year - nac.year - (
                (hoy.month, hoy.day) < (nac.month, nac.day) )
        return edad

