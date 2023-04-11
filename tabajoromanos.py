import unittest

def decimal_to_roman(decimal):
    total = '' 
    if decimal >= 100:
        centena = decimal // 100
        total = 'C' * centena
        decimal = decimal % 100 
        if centena == 400 :
            resultado = 'cd'
    if decimal >= 500:
        centena = decimal // 100
        total = 'd' * centena
        decimal = decimal % 100
        if centena == 900:
            resultado ='dm'
    if decimal == 1000:
        resultado = 'm'
    if decimal <= 3:
        total += 'I' * decimal
    elif decimal == 5:
        total += 'V'
    elif decimal == 10:
        total += "X"
    return total



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
        self.assertEqual(resultado,  'ccv')

    def test_trecientos(self):
        resultado = decimal_to_roman(300)
        self.assertEqual(resultado, 'ccc')
    
    def test_trecientos_tres(self):
        resultado = decimal_to_roman(303)
        self.assertEqual(resultado, 'ccciii')

    def test_trecientos_cinco(self):
        resultado = decimal_to_roman(305)
        self.assertEqual(resultado, 'cccv')
    
    def test_cuatrocientos(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, 'cd')
    
    def test_cuatrocientos_tres(self):
        resultado = decimal_to_roman(403)
        self.assertEqual(resultado, 'cdiii')

    def test_cuatrocientos(self):
        resultado = decimal_to_roman(400)
        self.assertEqual(resultado, 'cd')
    
    def test_cuatrocientos_tres(self):
        resultado = decimal_to_roman(403)
        self.assertEqual(resultado, 'cdiii')
    
    def test_cuatrocientos_cinco(self):
        resultado = decimal_to_roman(405)
        self.assertEqual(resultado, 'cdv')
    
    def test_quinientos(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'd')
    
    def test_quinientos_tres(self):
        resultado = decimal_to_roman(503)
        self.assertEqual(resultado, 'dii')

    def test_quinientos_cinco(self):
        resultado = decimal_to_roman(500)
        self.assertEqual(resultado, 'dv')
    
    def test_seisientos(self):
        resultado = decimal_to_roman(600)
        self.assertEqual(resultado, 'dc')
    
    def test_seisientos_tres(self):
        resultado = decimal_to_roman(603)
        self.assertEqual(resultado, 'dciii')
    
    def test_seisientos_cinco(self):
        resultado = decimal_to_roman(605)
        self.assertEqual(resultado, 'dcv')
    
    def test_setecientos(self):
        resultado = decimal_to_roman(700)
        self.assertEqual(resultado, 'dcc')
    
    def test_setecientos_tres(self):
        resultado = decimal_to_roman(703)
        self.assertEqual(resultado, 'dcciii')
    
    def test_setecientos_cinco(self):
        resultado = decimal_to_roman(705)
        self.assertEqual(resultado, 'dccv')
    
    def test_ochocientos(self):
        resultado = decimal_to_roman(800)
        self.assertEqual(resultado, 'dccc')
    
    def test_ochocientos_tres(self):
        resultado = decimal_to_roman(803)
        self.assertEqual(resultado, 'dccciii')
    
    def test_ochocientos_cinco(self):
        resultado = decimal_to_roman(805)
        self.assertEqual(resultado, 'dcccv')
    
    def test_novecientos(self):
        resultado = decimal_to_roman(900)
        self.assertEqual(resultado, 'dm')

    def test_novecientos_tres(self):
        resultado = decimal_to_roman(903)
        self.assertEqual(resultado, 'dmiii')

    def test_novecientos_cinco(self):
        resultado = decimal_to_roman(905)
        self.assertEqual(resultado, 'dmv')

    def test_mil(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'm')



if __name__ == '__main__':
    unittest.main()

