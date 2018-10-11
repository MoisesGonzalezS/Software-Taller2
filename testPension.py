import unittest
from datetime import date
from classPension import Pension

class Test(unittest.TestCase):

    def test_hombre_60_750sem_0InS(self):
        hoy = date.today()
        sesenta = hoy.replace(year=hoy.year-60)
        pensionado = Pension(sesenta, 'M', 750, 0)
        self.assertTrue( pensionado.cumple() )


if __name__ == "__main__":
    unittest.main()
