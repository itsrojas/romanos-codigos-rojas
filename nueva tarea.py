import unittest

def count_letters(word):
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result
def count_words(word):
    return {word: 1}


class TestCountLetters(unittest.TestCase):
    def test_words(self):
        result = count_words('hola')
        pruebas = count_letters('a','e','i','o','u')
        self.assertEqual(result, {'hola': 1;'a' })
    def test_1(self):
        result = count_letters('a')
        self.assertEqual(result, {'a': 1})
    def test_2(self):
        result = count_letters('e')
        self.assertEqual(result, {'e': 1})
    def test_3(self):
        result = count_letters('i')
        self.assertEqual(result, {'i': 1})
    def test_4(self):
        result = count_letters('o')
        self.assertEqual(result, {'o': 1})
    def test_5(self):
        result = count_letters('u')
        self.assertEqual(result, {'u': 1})



if __name__ == '__main__':
    unittest.main()
    
    
        

    

#HACER UN PROGRAMA QUE CUENTE LAS LETRAS DE UNA PALABRA Y QUE IMPRIMA LA PALABRA Y ALADO LOS NUMEROS
