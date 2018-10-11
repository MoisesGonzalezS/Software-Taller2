import unittest
from datetime import date
from classPension import Pension

class Test(unittest.TestCase):

    def test_hombre_60_750sem_0InS(self):
        hoy = date.today()
        nacimiento = hoy.replace(year=hoy.year-60)
        pensionado = Pension(nacimiento, 'M', 750, 0)
        self.assertTrue( pensionado.cumple() )

    def test_hombre_59_750sem_0Ins(self):
        hoy = date.today()
        nacimiento = hoy.replace(year=hoy.year-60, day=hoy.day+1)
        pensionado = Pension(nacimiento, 'M', 750, 0)
        self.assertFalse( pensionado.cumple() )

    def test_hombre60_749_sem_0Ins(self):
        hoy = date.today()
        nacimiento = hoy.replace(year=hoy.year-60)
        pensionado = Pension(nacimiento, 'M', 749, 0)
        self.assertFalse( pensionado.cumple() )

    def test_hombre59_749_sem_0Ins(self):
        hoy = date.today()
        nacimiento = hoy.replace(year=hoy.year-60, day=hoy.day+1)
        pensionado = Pension(nacimiento, 'M', 749, 0)
        self.assertFalse( pensionado.cumple() )

    def test_mujer55_750_sem_0Ins(self):
        hoy = date.today()
        nacimiento = hoy.replace(year=hoy.year-55)
        pensionado = Pension(nacimiento, 'F', 750, 0)
        self.assertTrue( pensionado.cumple() )

if __name__ == "__main__":
    unittest.main()
