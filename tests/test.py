import unittest
from src.main import validateMessage

class TestvalidateMessage(unittest.TestCase):
    def test_example(self):
        self.assertTrue(validateMessage("SOS", "PELIGROSOS"))
        self.assertTrue(validateMessage("HELP", "HELICOPTER"))
        self.assertFalse(validateMessage("RESCUE", "RSCU"))

    def test_uppercase_handling(self):
        self.assertTrue(validateMessage("TEST", "test"))
        self.assertTrue(validateMessage("test", "TEST"))
        self.assertTrue(validateMessage("TeSt", "tEsT"))

    def test_spaces_ignored(self):
        self.assertTrue(validateMessage("test", "test "))
        self.assertTrue(validateMessage("t es t", " test"))
        
    def test_special_characters(self):
        self.assertTrue(validateMessage("asd#", "asd#"))
        self.assertFalse(validateMessage("@@@#", "@@@@"))
        self.assertTrue(validateMessage("你好", "你你你哈好"))
        self.assertFalse(validateMessage("🧡🧡", "🧡"))

    def test_accented_characters(self):    
        self.assertTrue(validateMessage("Á", "á"))
        self.assertFalse(validateMessage("a", "Á"))

    def test_large_input(self):
        message = "a" * 10**6
        chest = "a" * 10**6
        chest2 = "b" * 10**6
        self.assertTrue(validateMessage(message, chest))
        self.assertFalse(validateMessage(message, chest2))

    def test_numbers(self):    
        self.assertTrue(validateMessage("asd9", "asd9"))
        self.assertFalse(validateMessage("asd9", "asd8"))