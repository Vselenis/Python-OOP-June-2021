from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory

class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.pf = PaintFactory("Test", 100)

    def test_init(self):
        pf = PaintFactory("Test", 100)
        self.assertEqual("Test", pf.name)
        self.assertEqual(100, pf.capacity)
        self.assertEqual({}, pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    def test_add_ingredient_invalid_product_type(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient("purple", 2)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_invalid_product_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient("white", 5000)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_all_correct(self):
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.pf.ingredients)
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 4}, self.pf.ingredients)


    def test_remove_ingredient_invalid_product(self):
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient("asd", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_invalid_quantity(self):
        self.pf.add_ingredient("blue", 6)
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient("blue", 765)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_valid(self):
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.pf.ingredients)
        self.pf.remove_ingredient("white", 2)
        self.assertEqual({"white": 0}, self.pf.ingredients)


if __name__ == "__main__":
    main()