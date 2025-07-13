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
        
