from unittest import TestCase
from project1.mammal import Mammal

class TestMammal(TestCase):
    def test_init(self):
        mammal = Mammal("Gosho", "Dog", "Bao")
        self.assertEqual(mammal.name, "Gosho")
        self.assertEqual(mammal.type, "Dog")
        self.assertEqual(mammal.sound, "Bao")
        self.assertEqual(mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        mammal = Mammal("Gosho", "Dog", "Bao")
        res = mammal.make_sound()
        self.assertEqual(res, "Gosho makes Bao")

    def test_get_kingdom(self):
        mammal = Mammal("Gosho", "Dog", "Bao")
        res = mammal.get_kingdom()
        self.assertEqual(res, "animals")

    def test_info(self):
        mammal = Mammal("Gosho", "Dog", "Bao")
        res = mammal.info()
        self.assertEqual(res, f"Gosho is of type Dog")