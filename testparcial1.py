import unittest

from Paarcial1 import contadorFrecuencia

class TestContadorfrecuencia(unittest.TestCase):
#self este contador es como llamar un lista con self pero como la variable es verdadera self es como las cualidades o una lista que cosas que hacemos 
#en pocas palabras llamamos a una clase con su cualidades pero no tenemos culidades tenemos ejercisios
#con los ejemplos vemos que es una cadena seguia y identificamos la palbras que uno repite 
    def test_contador_frecuencia(self):
        self.assertEqual(contadorFrecuencia('Esta es la prueba de esta ocasión'), {'esta': 2, 'es': 1, 'la': 1, 'prueba': 1, 'de': 1, 'ocasión': 1})
        self.assertEqual(contadorFrecuencia('hola hola hola '), {"hola":3})
        self.assertEqual(contadorFrecuencia('000 000 999 999'), {'000': 2, '999': 2})
        self.assertEqual(contadorFrecuencia('Estaesunaoracionsinespaciosporquelabarraespaciadoradejodefuncionar'), {'estaesunaoracionsinespaciosporquelabarraespaciadoradejodefuncionar': 1})
        self.assertEqual(contadorFrecuencia('hola a todos hola'), {'hola': 2, 'a': 1, 'todos': 1})
        self.assertEqual(contadorFrecuencia("rapido rapido furioso furioso"),{"rapido": 2, "furioso": 2 })
        self.assertEqual(contadorFrecuencia("angel angel que haces tan noche trabajando"),{"angel": 2, "que": 1, "haces": 1, "tan" : 1, "noche": 1 ,"trabajando":1 })
        self.assertEqual(contadorFrecuencia("pura pura pura vidaa"),{"pura":3, "vidaa":1})
        self.assertEqual(contadorFrecuencia("sere alguien algun dia"),{"sere": 1,"alguien": 1,"algun": 1, "dia": 1})
        self.assertEqual(contadorFrecuencia("cada noche de noche es genial"),{"cada": 1, "noche": 2, "de": 1, "es": 1, "genial": 1 })



#son dos formas que son parecidas pero nesecito pulir mas aprender mas para acortarlo 



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# aqui contamos y cormamos cuantas palabras se epiten 
    def test_contadorFrecuencia():
       assert contadorFrecuencia("Esta es la prueba de esta ocasión") == {
        "Esta": 1, "es": 1, "la": 1, "prueba": 1, "de": 1, "esta": 1, "ocasión": 1
        }
# cuando vemos la lista vacia algunos les tira erro pero a otros les tira una lista vacia 
       assert contadorFrecuencia("") == {}
       assert contadorFrecuencia("000 000 999 999") == {"000": 2, "999": 2}
# esta es una de las palabras de maxima frecuencia 
       assert contadorFrecuencia("Estaesunaoracionsinespaciosporquelabarraespaciadoradejodefuncionar") == {
        "Estaesunaoracionsinespaciosporquelabarraespaciadoradejodefuncionar": 1
        }
# de aqui vamos mismo patron asegurando que todo este en la cantida de palabras que se repite 

       assert contadorFrecuencia("Feliz Navidad Feliz Navidad prospero año y felicidad") == {
        "Feliz": 2, "Navidad": 2, "prospero": 1, "año": 1, "y": 1, "felicidad": 1
        }
       assert contadorFrecuencia("Feliz Halloween a todos Feliz Halloween") == {
        "Feliz": 2, "Halloween": 2, "a": 1, "todos": 1
        }
       assert contadorFrecuencia("Santa Claus viene a la ciudad Santa Claus Santa") == {
        "Santa": 3, "Claus": 2, "viene": 1, "a": 1, "la": 1, "ciudad": 1
        }
#aqui vemos que un truco es mayuscula y el otro minuscula asi que no es una palbra repetida truco 
#porque el programa tambien ve si es mayuscula si lleva tilde todo marca una diferencia 
       assert contadorFrecuencia("Truco o trato truco o trato truco") == {
        "Truco": 1, "o": 2, "trato": 2, "truco": 1
        }
       assert contadorFrecuencia("Navidad blanca Navidad blanca") == {
        "Navidad": 2, "blanca": 2
        }
       assert contadorFrecuencia("Noche de paz noche de amor") == {
        "Noche": 1, "de": 2, "paz": 1, "noche": 1, "amor": 1
        }

if __name__ == '__main__':
    unittest.main()