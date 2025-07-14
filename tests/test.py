import unittest
from src.main import validacionMensaje

class TestValidacionMensaje(unittest.TestCase):
    def test_ejemplo(self):
        self.assertTrue(validacionMensaje("SOS", "PELIGROSOS"))
        self.assertTrue(validacionMensaje("HELP", "HELICOPTER"))
        self.assertFalse(validacionMensaje("RESCUE", "RSCU"))

    def test_mayusculas(self):
        self.assertTrue(validacionMensaje("TEST", "test"))
        self.assertTrue(validacionMensaje("test", "TEST"))
        self.assertTrue(validacionMensaje("TeSt", "tEsT"))

    def test_espacios(self):
        self.assertTrue(validacionMensaje("test", "test "))
        self.assertTrue(validacionMensaje("t es t", " test"))
        
    def test_caracteres_especiales(self):
        self.assertFalse(validacionMensaje("asd#", "asd#"))
        self.assertFalse(validacionMensaje("@@@", "@@@@"))

        
    def test_acentos(self):    
        self.assertTrue(validacionMensaje("Á", "á"))
        self.assertFalse(validacionMensaje("a", "Á"))
        
    def test_muchos_caracteres(self):
        mensaje = "a" * 10**6
        cofre = "a" * 10**6
        cofre2 = "b" * 10**6
        self.assertTrue(validacionMensaje(mensaje, cofre))
        self.assertFalse(validacionMensaje(mensaje, cofre2))
        
    def test_numeros(self):    
        self.assertTrue(validacionMensaje("asd9", "asd9"))
        self.assertFalse(validacionMensaje("asd9", "asd8"))
        