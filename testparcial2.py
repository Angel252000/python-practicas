import unittest

from paarcial2 import cuadrado,trianguloderecho,diamante 
    
class TestFiguras(unittest.TestCase):
#test del cuadrado de manera corta 
#cuando hacemos la forma de cuadrado too lleva un patron 3 de largo 3 de ancho y haci formamos nuestra figura 
    def test_cuadrado(self):
        self.assertEqual(cuadrado(3), [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]])
        self.assertEqual(cuadrado(5), [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]])
        self.assertEqual(cuadrado(7), [["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", '*'], ["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*"]])
#test del triangulo derecho de manera mas corta
# el triangulo derecho en este caso vamos normalmente 1 2 3 
#pero como lo voy diciendo nuestra forma de pensar en codigos es indeterminada 
#cada uno piensa distinto pero van por el mismo camino
    def test_triangulo_derecho(self):
        self.assertEqual(trianguloderecho(3), [["*"], ["*", "*"], ["*", "*", "*"]])
        self.assertEqual(trianguloderecho(5), [["*"], ["*", "*"], ["*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*", "*"]])
        self.assertEqual(trianguloderecho(7), [["*"], ["*", "*"], ["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*", "*"]])
#test del diamante de manera corta
#cuando ocupamos este test formamos nostros mismos como lo queremos 
#en este caso cuando llamamos a self lo llamamos como una clase 
# entonces self seria como los objetos o las cosas que identificamos o podremos vr la clase y el obejeto de forma de test
    def test_diamante(self):
        self.assertEqual(diamante(3), [["*"], ["*","*"], ["*"]])
        self.assertEqual(diamante(5), [["*"], ["*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*"], ["*"]] )
        self.assertEqual(diamante(7), [["*"], ["*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*" ,"*" ,"*"], ["*", "*", "*", "*", "*"], ["*", "*", "*"], ["*"]])
        self.assertEqual( diamante(9),[["*"], ["*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*"], ["*"]])

#ocupamos dos formas uno que viene en cadena que ocupa la misma logica que la primera 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def test_cuadrado():
    # Cuadrado el cuadrado lo llamamos 3*3 mismo 3 de largo y de ancho pero lo que yo llamo es el resultado 
    #si voy formando correctamente el cuadrado 
    resultado_cuadrado_3 = cuadrado(3)
    assert resultado_cuadrado_3 == "***\n***\n***", f"Esperado:\n{resultado_cuadrado_3}"

    resultado_cuadrado_5 = cuadrado(5)
    assert resultado_cuadrado_5 == "*****\n*****\n*****\n*****\n*****", f"Esperado:\n{resultado_cuadrado_5}"

    resultado_cuadrado_7 = cuadrado(7)
    assert resultado_cuadrado_7 == "*******\n*******\n*******\n*******\n*******\n*******\n*******", f"Esperado:\n{resultado_cuadrado_7}"

def test_triangulo_derecho():
    # Triángulos derechos igual manera pero como cambia la forma tenemos que hallarle sentido
    #voy uno por uno formando la figura que voy haciendo 
    resultado_triangulo_3 = trianguloderecho(3)
    assert resultado_triangulo_3 == "*\n**\n***", f"Esperado:\n{resultado_triangulo_3}"

    resultado_triangulo_5 = trianguloderecho(5)
    assert resultado_triangulo_5 == "*\n**\n***\n****\n*****", f"Esperado:\n{resultado_triangulo_5}"

    resultado_triangulo_7 = trianguloderecho(7)
    assert resultado_triangulo_7 == "*\n**\n***\n****\n*****\n******\n*******", f"Esperado:\n{resultado_triangulo_7}"

def test_diamante():
    # Diamantes tengo que haya una forma que yo tenga un diamante para que me salga 3 de largo y ancho
    # voy midiendo 1 3 1 y me da la forma de diamnte y cumplo con los criterios 
    #se forma y se el resultado 
    resultado_diamante_3 = diamante(3)
    assert resultado_diamante_3 == "*\n***\n*", f"Esperado:\n{resultado_diamante_3}"

    resultado_diamante_5 = diamante(5)
    assert resultado_diamante_5 == "*\n***\n*****\n***\n*", f"Esperado:\n{resultado_diamante_5}"

    resultado_diamante_7 = diamante(7)
    assert resultado_diamante_7 == "*\n***\n*****\n*******\n*****\n***\n*", f"Esperado:\n{resultado_diamante_7}"

    resultado_diamante_9 = diamante(9)
    assert resultado_diamante_9 == "*\n***\n*****\n*******\n*********\n*******\n*****\n***\n*", f"Esperado:\n{resultado_diamante_9}"
# lo puse al reves primero era assert y luego resultado 
    test_cuadrado()
    test_triangulo_derecho()
    test_diamante()
    print("Todos los tests han pasado correctamente.")


if __name__ == '__main__':
    unittest.main()