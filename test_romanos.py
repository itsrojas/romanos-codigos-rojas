import unittest
from decimales_a_romanos import decimal_to_roman
from romanos_a_decimales import roman_to_decimal

class testdecimaltoroman(unittest.testcase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')
    
    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado,  "iv")

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_ciento_uno(self):
        resultado = decimal_to_roman(101)
        self.assertEqual(resultado, 'CI')

    def test_ciento_tres(self):
        resultado = decimal_to_roman(103)
        self.assertEqual(resultado, 'CIII')

    def test_ciento_cinco(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado, 'CV')

    def test_ciento_diez(self):
        resultado = decimal_to_roman(110)
        self.assertEqual(resultado, 'CX')
    
    def test_docientos(self):
        resultado = decimal_to_roman(200)
        self.assertEqual(resultado, 'CC')

    def test_docientos_tres(self):
        resultado = decimal_to_roman(203)
        self.assertEqual(resultado, 'CCIII')
    
    def test_docientos_cinco(self):
        resultado = decimal_to_roman(205)
        self.assertEqual(resultado,  'CCV')

    def test_trecientos(self):
        resultado = decimal_to_roman(300)
        self.assertEqual(resultado, 'CCC')
    
    def test_trecientos_tres(self):
        resultado = decimal_to_roman(303)
        self.assertEqual(resultado, 'CCCIII')

    def test_trecientos_cinco(self):
        resultado = decimal_to_roman(305)
        self.assertEqual(resultado, 'CCCV')
    
    def test_cuatrocientos(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, 'CD')
    
    def test_cuatrocientos_tres(self):
        resultado = decimal_to_roman(403)
        self.assertEqual(resultado, 'CDIII')

    def test_cuatrocientos(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, 'CD')
    
    def test_cuatrocientos_tres(self):
        resultado = decimal_to_roman(403)
        self.assertEqual(resultado, 'CDIII')
    
    def test_cuatrocientos_cinco(self):
        resultado = decimal_to_roman(405)
        self.assertEqual(resultado, 'CDV')
    
    def test_quinientos(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'D')
    
    def test_quinientos_tres(self):
        resultado = decimal_to_roman(503)
        self.assertEqual(resultado, 'DIII')

    def test_quinientos_cinco(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'DV')
    
    def test_seisientos(self):
        resultado = decimal_to_roman(600)
        self.assertEqual(resultado, 'DC')
    
    def test_seisientos_tres(self):
        resultado = decimal_to_roman(603)
        self.assertEqual(resultado, 'DCIII')
    
    def test_seisientos_cinco(self):
        resultado = decimal_to_roman(605)
        self.assertEqual(resultado, 'DCV')
    
    def test_setecientos(self):
        resultado = decimal_to_roman(700)
        self.assertEqual(resultado, 'DCC')
    
    def test_setecientos_tres(self):
        resultado = decimal_to_roman(703)
        self.assertEqual(resultado, 'DCCIII')
    
    def test_setecientos_cinco(self):
        resultado = decimal_to_roman(705)
        self.assertEqual(resultado, 'DCCV')
    
    def test_ochocientos(self):
        resultado = decimal_to_roman(800)
        self.assertEqual(resultado, 'DCCC')
    
    def test_ochocientos_tres(self):
        resultado = decimal_to_roman(803)
        self.assertEqual(resultado, 'DCCCIII')
    
    def test_ochocientos_cinco(self):
        resultado = decimal_to_roman(805)
        self.assertEqual(resultado, 'DCCCV')
    
    def test_novecientos(self):
        resultado = decimal_to_roman(900)
        self.assertEqual(resultado, 'DM')

    def test_novecientos_tres(self):
        resultado = decimal_to_roman(903)
        self.assertEqual(resultado, 'DMIII')

    def test_novecientos_cinco(self):
        resultado = decimal_to_roman(905)
        self.assertEqual(resultado, 'DMV')

    def test_mil(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)

    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)

    def test_IV(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)

    def test_V(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)

    def test_VI(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)

    def test_VII(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)

    def test_VIII(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)

    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)
    
    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)

    def test_XI(self):
        resultado = roman_to_decimal('XLIII')
        self.assertEqual(resultado, 43)

    def test_XII(self):
        resultado = roman_to_decimal('CCI')
        self.assertEqual(resultado, 201)

    def test_XIII(self):
        resultado = roman_to_decimal('CCCLCIX')
        self.assertEqual(resultado, 399)

    def test_XIV(self):
        resultado = roman_to_decimal('CDLVIII')
        self.assertEqual(resultado, 458)

    def test_XV(self):
        resultado = roman_to_decimal('D')
        self.assertEqual(resultado, 500)

    def test_XVI(self):
        resultado = roman_to_decimal('DCCVI')
        self.assertEqual(resultado, 706)

    def test_XVII(self):
        resultado = roman_to_decimal('M')
        self.assertEqual(resultado, 1000)

    def test_XVIII(self):
        resultado = roman_to_decimal('MMMCDLXXXIX')
        self.assertEqual(resultado, 3489)

if  __name__  == '__main__':
    unittest.main